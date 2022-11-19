import "./trip-card.styles.scss";

const TripCard = (trip) => {
  console.log("Trip is:", trip);
  const { title, thumbnail_image } = trip.trip;
  console.log(title);
  return (
    <div>
      <h3>{title}</h3>
      <img className="thumbnail" src={thumbnail_image} />
    </div>
  );
};

export default TripCard;
