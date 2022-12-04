import { render, getByText } from "@testing-library/react";
import TripCard from "./trip-card.component";

test("contains the trip title", () => {
  const test_input = {
    title: "Title 1",
    description: "Description 1",
    dates: "Dates 1",
    splash_image: "image_url",
    thumbnail_image: "thumb_url",
  };
  const { getByText } = render(<TripCard trip={test_input} />);
  const title = getByText(test_input.title);
  expect(title).toBeInTheDocument();
});
