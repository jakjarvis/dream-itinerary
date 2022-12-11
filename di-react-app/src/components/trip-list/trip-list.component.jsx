import "./trip-list.styles.css";
import TripCard from "../trip-card/trip-card.component";

const TripList = (trips) => {
  return (
    <div className="trips-list" data-testid="trips-list">
      {trips.trips.map((trip) => {
        return <TripCard className="tripCard" trip={trip} />;
      })}
    </div>
  );
};

export default TripList;
