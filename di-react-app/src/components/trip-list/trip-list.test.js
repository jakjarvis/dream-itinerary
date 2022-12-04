import { render } from "@testing-library/react";
import { within } from "@testing-library/dom";
import TripList from "./trip-list.component";

test("returns trip card for each trip returned from backend", () => {
  const test_input = [
    {
      title: "Title 1",
      description: "Description 1",
      dates: "Dates 1",
      splash_image: "image_url",
      thumbnail_image: "thumb_url",
    },
    {
      title: "Title 2",
      description: "Description 2",
      dates: "Dates 2",
      splash_image: "image_url",
      thumbnail_image: "thumb_url",
    },
  ];
  const { getAllByTestId } = render(<TripList trips={test_input} />);
  const cards = getAllByTestId("trip-card");
  expect(cards.length).toEqual(test_input.length);
});
