import { useState, useEffect } from "react";
import axios from "axios";

import MemoryGrid from "./components/MemoryGrid";
import RiskGauge from "./components/RiskGauge";
import StatsChart from "./components/StatsChart";
import AlgorithmSelector from "./components/AlgorithmSelector";
import WorkloadGenerator from "./components/WorkloadGenerator";

export default function App() {
  const [data, setData] = useState(null);
  const [history, setHistory] = useState([]);
  const [running, setRunning] = useState(false);
  const [algorithm, setAlgorithm] = useState("LRU");

  useEffect(() => {
    if (!running) return;

    console.log("🚀 SIMULATION STARTED");

    const interval = setInterval(() => {
      const randomPage = Math.floor(Math.random() * 10);

      axios
        .post("http://localhost:8000/access", {
          page: randomPage,
          algorithm: algorithm,
        })
        .then((res) => {
          console.log("API RESPONSE:", res.data);

          setData(res.data);

          setHistory((prev) => [
            ...prev,
            {
              step: prev.length + 1,
              faults: res.data.stats.faults,
              hits: res.data.stats.hits,
            },
          ]);
        })
        .catch((err) => {
          console.error("❌ API ERROR:", err);
        });
    }, 1000);

    return () => {
      console.log("⛔ SIMULATION STOPPED");
      clearInterval(interval);
    };
  }, [running, algorithm]);

  return (
    <div className="bg-black text-white min-h-screen p-6">
      <h1 className="text-3xl font-bold mb-4">
        NeuroVM AI Dashboard
      </h1>

      <div className="flex gap-4 mb-4">
        <button
          className="bg-green-500 px-4 py-2"
          onClick={() => setRunning(true)}
        >
          Start
        </button>

        <button
          className="bg-red-500 px-4 py-2"
          onClick={() => setRunning(false)}
        >
          Stop
        </button>
      </div>

      <AlgorithmSelector setAlgorithm={setAlgorithm} />
      <WorkloadGenerator />

      {data && (
        <div className="grid grid-cols-2 gap-6 mt-6">
          <MemoryGrid frames={data.memory_event.frames} />
          <RiskGauge prediction={data.prediction} />
          <StatsChart history={history} />

          <div className="bg-gray-800 p-4 rounded">
            <h3>Optimization</h3>
            <p>{data.optimization.action}</p>
            <p>Frames: {data.optimization.new_frame_count}</p>
          </div>
        </div>
      )}
    </div>
  );
}