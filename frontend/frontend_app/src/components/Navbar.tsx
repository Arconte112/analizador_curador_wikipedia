import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4 text-white">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/" className="text-xl font-bold">
          Wikipedia Analyzer
        </Link>
        <div className="space-x-4">
          <Link href="/" className="hover:text-gray-300">
            Search
          </Link>
          <Link href="/saved" className="hover:text-gray-300">
            Saved Articles
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
