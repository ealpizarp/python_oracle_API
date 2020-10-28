import Bar from './components/Bar'
import "bootstrap/dist/css/bootstrap.min.css" 
import Peliculas from './components/Peliculas'

function App() {
  return (
    <div className="App">
      <header className="App-header">
       <Bar /> 
       <Peliculas/>
      </header>
    </div>
  );
}

export default App;
