export default function Loading() {
  return (
    <div className="panel loading">
      <p>Loading…</p>
      <div className="skeleton" style={{ width: '60%' }} />
      <div className="skeleton" style={{ width: '80%' }} />
      <div className="skeleton" style={{ width: '40%' }} />
    </div>
  );
}
