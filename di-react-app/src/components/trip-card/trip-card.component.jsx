import "./trip-card.styles.css";

const TripCard = (trip) => {
  const { title, thumbnail_image } = trip.trip;
  return (
    <div className="trip-card" data-testid="trip-card">
      <h4>{title}</h4>
      <img className="thumbnail" src={thumbnail_image} />
    </div>
  );
};

export default TripCard;
