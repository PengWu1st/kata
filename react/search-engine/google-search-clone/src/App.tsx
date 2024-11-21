import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");

  const handleSearch = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    alert(`Searching for: ${query}`);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-8">Google Search Clone</h1>
      <form onSubmit={handleSearch} className="w-full max-w-md">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full p-4 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Search..."
        />
        <button
          type="submit"
          className="mt-4 w-full p-4 bg-blue-500 text-white rounded-lg shadow-sm hover:bg-blue-600"
        >
          Search
        </button>
      </form>
    </div>
  );
}

export default App;
