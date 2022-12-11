import { useEffect, useState } from "react";
import TripCard from "../../components/trip-card/trip-card.component";

const Home = () => {
  const [trips, setTrips] = useState([{}]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/trips")
      .then((response) => response.json())
      .then((trips) => setTrips(trips));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Here are your upcoming Trips!</h1>
        <div className="trips-list">
          {trips.map((trip) => {
            return <TripCard trip={trip} />;
          })}
        </div>
      </header>
    </div>
  );
};
export default Home;
