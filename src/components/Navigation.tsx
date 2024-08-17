import Link from "next/link";
import { useRouter } from "next/router";
import NavItem from "./NavItem";

export default function Navigation() {
  return (
    <nav className="flex justify-between px-3 items-center h-16 bg-red-950">
      <Link href="/">McMaster Computer Science Visualizer</Link>
      <ul className="flex h-full py-3 items-center justify-end gap-3">
        <NavItem href="/about">About</NavItem>
        <NavItem href="/courses">Courses</NavItem>
        <NavItem href="/visualizer">Visualizer</NavItem>
        <NavItem href="/resources">Resources</NavItem>
        <NavItem href="/calendar">Calendar</NavItem>
      </ul>
    </nav>
  );
}
