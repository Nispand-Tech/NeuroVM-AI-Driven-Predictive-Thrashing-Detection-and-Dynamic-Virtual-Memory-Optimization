export default function MemoryGrid({ frames }) {
  return (
    <div>
      <h2>Memory Heatmap</h2>
      <div className="flex gap-2">
        {frames.map((f, i) => (
          <div
            key={i}
            className="w-16 h-16 flex items-center justify-center rounded"
            style={{
              background: `rgba(0,255,0,${(i + 1) / frames.length})`,
            }}
          >
            {f}
          </div>
        ))}
      </div>
    </div>
  );
}