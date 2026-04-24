import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

export default function StatsChart({ history }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h2>Performance Trend</h2>
      <LineChart width={700} height={300} data={history}>
        <XAxis dataKey="step" />
        <YAxis />
        <Tooltip />
        <CartesianGrid strokeDasharray="3 3" />
        <Line type="monotone" dataKey="faults" />
        <Line type="monotone" dataKey="hits" />
      </LineChart>
    </div>
  );
}