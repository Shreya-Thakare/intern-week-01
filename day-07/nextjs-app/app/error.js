'use client';

export default function Error({ error, reset }) {
  return (
    <div className="panel">
      <h1>Something went wrong</h1>
      <p className="error" style={{ marginTop: '1rem' }}>{error?.message || 'Unexpected error'}</p>
      <button className="btn btn-primary" style={{ marginTop: '1rem' }} onClick={() => reset()}>
        Try again
      </button>
    </div>
  );
}
