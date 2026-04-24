export default function AlgorithmSelector({ setAlgorithm }) {
  return (
    <div className="mb-4">
      <h2>Select Algorithm</h2>
      <select
        className="text-black p-2"
        onChange={(e) => setAlgorithm(e.target.value)}
      >
        <option>LRU</option>
        <option>FIFO</option>
        <option>OPTIMAL</option>
        <option>AI</option>
      </select>
    </div>
  );
}