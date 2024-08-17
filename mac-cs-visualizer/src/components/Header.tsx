export default function Header() {
  return (
    <header className="flex justify-start items-center h-16 bg-stone-800">
      <a
        id="logo"
        className="flex items-center justify-center h-16 w-grow px-3 bg-stone-700 text-white"
        href="/"
      >
        McMaster Computer Science Visualizer
      </a>
    </header>
  );
}
