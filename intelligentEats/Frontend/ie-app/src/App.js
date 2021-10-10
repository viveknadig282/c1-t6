import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  // Link
} from "react-router-dom";
import Barscan from './pages/BarcodeScanner'

function App() {
  return (
    <div className="App">
        <Router>
          <div>
            <Switch>
              <Route path="/barcode_scanner">
                <Barscan/>
              </Route>
            </Switch>
          </div>
        </Router>
    </div>
  );
}

export default App;
