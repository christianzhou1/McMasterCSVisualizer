import Link from "next/link";
import React from "react";

interface NavItemProps {
  href: string;
  children: React.ReactNode;
}

export default function NavItem({ href, children }: NavItemProps) {
  return (
    <li className="flex items-center justify-center h-16 w-grow px-3 bg-stone-700 text-white">
      <Link href={href}>{children}</Link>
    </li>
  );
}
