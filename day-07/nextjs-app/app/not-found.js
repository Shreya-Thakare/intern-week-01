import Link from 'next/link';

export default function NotFound() {
  return (
    <main className="panel">
      <h1>Employee not found</h1>
      <p className="sub">The record may have been deleted.</p>
      <Link href="/employees" className="btn btn-primary">
        Back to employees
      </Link>
    </main>
  );
}
