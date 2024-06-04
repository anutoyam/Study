import asyncio

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    async def handle_client(self, reader, writer):
        self.clients.append(writer)
        while True:
            data = await reader.read(100)
            message = data.decode().strip()
            if message == 'exit':
                writer.close()
                self.clients.remove(writer)
                break
            await self.broadcast(message)

    async def broadcast(self, message):
        for client in self.clients:
            client.write(message.encode())
            await client.drain()

    async def run(self):
        server = await asyncio.start_server(
            self.handle_client, self.host, self.port)

        async with server:
            await server.serve_forever()

class ChatClient:
    async def read_input(self):
        while True:
            message = await asyncio.get_event_loop().run_in_executor(None, input)
            await self.send_message(message)

    async def send_message(self, message):
        try:
            reader, writer = await asyncio.open_connection(
                self.host, self.port)
            writer.write(message.encode())
            await writer.drain()
            writer.close()
            await writer.wait_closed()
        except ConnectionRefusedError:
            print("서버에 연결할 수 없습니다.")

    async def run(self, host, port):
        self.host = host
        self.port = port
        await asyncio.gather(self.read_input(), self.send_message("connected"))

host = 'localhost'
port = 8888

async def main():
    server = ChatServer(host, port)
    chat_server_task = asyncio.create_task(server.run())

    client = ChatClient()
    chat_client_task = asyncio.create_task(client.run(host, port))

    await asyncio.gather(chat_server_task, chat_client_task)

asyncio.run(main())
