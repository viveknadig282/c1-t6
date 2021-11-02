import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  // Link
} from "react-router-dom";
import BarcodeScanner from './Components/Scanner/BarcodeScanner';
import Navbar from './Components/Navbar/Navbar';
import Results from './pages/Results';

function App() {
  return (
    <div className="App">
        <Router>
          <div>
            <Switch>
              <Route path="/results">
                <Results/>
              </Route>
            </Switch>
          </div>
        </Router>
        {/* <Navbar/>
        <BarcodeScanner/> */}
    </div>
  );
}

export default App;
