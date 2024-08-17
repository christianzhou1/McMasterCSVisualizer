import Link from "next/link";
import { useRouter } from "next/router";
import NavItem from "./NavItem";

export default function Navigation() {
  return (
    <nav className="flex justify-between items-center h-16 bg-stone-800">
      <Link href="/">McMaster Computer Science Visualizer</Link>
      <ul className="flex items-center justify-end">
        <NavItem href="/about">About</NavItem>
        <NavItem href="/courses">Courses</NavItem>
        <NavItem href="/calendar">Calendar</NavItem>
      </ul>
    </nav>
  );
}
