'use client';

import { useRouter } from 'next/navigation';
import { useState } from 'react';
import Link from 'next/link';
import { createEmployee } from '../../../lib/api';

export default function CreateEmployeePage() {
  const router = useRouter();
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);

  async function onSubmit(e) {
    e.preventDefault();
    setError('');
    setBusy(true);
    const form = Object.fromEntries(new FormData(e.currentTarget));
    form.salary = Number(form.salary);
    try {
      const created = await createEmployee(form);
      router.push(`/employees/${created.id}`);
      router.refresh();
    } catch (err) {
      setError(err.message);
      setBusy(false);
    }
  }

  return (
    <main>
      <h1>Create employee</h1>
      <p className="sub">POST /api/employees</p>

      <div className="panel">
        <form className="form" onSubmit={onSubmit}>
          <label>
            Name
            <input name="name" required placeholder="Full name" />
          </label>
          <label>
            Email
            <input name="email" type="email" required placeholder="name@example.com" />
          </label>
          <label>
            Department
            <input name="department" required placeholder="Engineering" />
          </label>
          <label>
            Position
            <input name="position" required placeholder="Developer" />
          </label>
          <label>
            Salary (₹)
            <input name="salary" type="number" min={1} required placeholder="50000" />
          </label>

          {error && <div className="error">{error}</div>}

          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button className="btn btn-primary" type="submit" disabled={busy}>
              {busy ? 'Saving…' : 'Save'}
            </button>
            <Link href="/employees" className="btn btn-ghost">
              Cancel
            </Link>
          </div>
        </form>
      </div>
    </main>
  );
}
