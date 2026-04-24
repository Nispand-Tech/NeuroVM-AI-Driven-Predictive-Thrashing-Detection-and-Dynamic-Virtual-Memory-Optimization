export default function RiskGauge({ prediction }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h2>AI Thrashing Risk</h2>
      <h3>{prediction.state}</h3>
      <p>Risk Score: {prediction.risk}</p>
    </div>
  );
}