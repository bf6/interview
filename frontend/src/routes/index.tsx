import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  component: Index,
});

export function Index() {
  return <>Hello World</>;
}
