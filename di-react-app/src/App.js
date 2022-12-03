import "./App.css";
import { useEffect, useState } from "react";
import TripList from "./components/trip-list/trip-list.component";

const App = () => {
  const [trips, setTrips] = useState([{}]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/trips")
      .then((response) => response.json())
      .then((trips) => setTrips(trips));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Here are your upcoming Trips!!</h1>
        <TripList trips={trips} />
      </header>
    </div>
  );
};
export default App;
