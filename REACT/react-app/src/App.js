import './App.css';

function Header(props) {
  return <header>
  <h1><a href='/'>{props.title}</a></h1>
</header>
}

function Nav(props ) {
  return <nav>
  <li><a href="/read/{props.id}">{props.title}</a></li>
</nav>
}

function Article(props) {
  return<article>
  <h2>{props.title}</h2>
    {props.body}
  </article>

}

function App() {
  const topic = [
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'javascript', body:'javascript is ...'}
  ]
  return (
    <div>
      <Header title = "React test!"></Header>
      <Nav ></Nav>
      <Article title = "Welcome" body = "Hello, Web!"></Article>
    </div>
  );
}

export default App;
