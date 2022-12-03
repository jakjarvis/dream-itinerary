import { render } from "@testing-library/react";

import App from "./App";

test("displays trip list on home page", () => {
  const { getByTestId } = render(<App />);
  const tripList = getByTestId("trips-list");
  expect(tripList).toBeInTheDocument();
});
