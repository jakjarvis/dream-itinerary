import { getByTitle } from "@testing-library/react";

const TripCard = (trip) => {
  console.log("Trip is:", trip);
  const { title, thumbnail_image } = trip.trip;
  console.log(title);
  return (
    <div>
      <h3>{title}</h3>
      <img src={thumbnail_image} />
    </div>
  );
};

export default TripCard;
