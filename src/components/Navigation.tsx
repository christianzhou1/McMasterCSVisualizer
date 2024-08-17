import Link from "next/link";
import { useRouter } from "next/router";
import NavItem from "./NavItem";

export default function Navigation() {
  return (
    <nav className="flex sm:justify-between sm:flex-row flex-col px-3 items-center sm:h-16 h-full bg-mac-dark-red">
      <Link href="/">McMaster Computer Science Visualizer</Link>
      <ul className="flex sm:flex-row flex-col h-full py-3 items-center md:gap-3 gap-1 md:px-0">
        <NavItem href="/about">About</NavItem>
        <NavItem href="/courses">Courses</NavItem>
        <NavItem href="/visualizer">Visualizer</NavItem>
        <NavItem href="/resources">Resources</NavItem>
        <NavItem href="/calendar">Calendar</NavItem>
      </ul>
    </nav>
  );
}
