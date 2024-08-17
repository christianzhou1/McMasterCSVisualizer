import Link from "next/link";
import React from "react";

interface NavItemProps {
  href: string;
  children: React.ReactNode;
}

export default function NavItem({ href, children }: NavItemProps) {
  return (
    <li className="min-w-20 h-full bg-stone-800 text-white">
      <Link
        href={href}
        className="flex justify-center items-center h-full w-full bg-red-600"
      >
        {children}
      </Link>
    </li>
  );
}
