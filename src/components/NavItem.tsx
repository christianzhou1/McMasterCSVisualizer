import Link from "next/link";
import React from "react";

interface NavItemProps {
  href: string;
  children: React.ReactNode;
}

export default function NavItem({ href, children }: NavItemProps) {
  return (
    <li className="sm:w-24 w-24 h-full bg-stone-800 text-white">
      <Link
        href={href}
        className="flex justify-center items-center h-full w-full bg-mac-yellow text-black"
      >
        {children}
      </Link>
    </li>
  );
}
