import './App.css';

function Header() {
  return <header>
  <h1><a href='/'>React</a></h1>
</header>
}

function Nav() {
  return <nav>
  <li><a href="/read/1">html</a></li>
  <li><a href="/read/2">css</a></li>
  <li><a href="/read/3">js</a></li>
</nav>
}

function Article() {
  return<article>
  <h2>Welcome</h2>
    Hello, WEB
  </article>

}

function App() {
  return (
    <div>
      <Header></Header>
      <Header></Header>
      <Header></Header>
      <Nav></Nav>
      <Article></Article>
    </div>
  );
}

export default App;
