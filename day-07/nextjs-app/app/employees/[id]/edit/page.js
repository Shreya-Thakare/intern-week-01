'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { API_BASE, updateEmployee } from '../../../../lib/api';

export default function EditEmployeePage() {
  const { id } = useParams();
  const router = useRouter();
  const [form, setForm] = useState(null);
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch(`${API_BASE}/employees/${id}`, { cache: 'no-store' });
        if (!res.ok) throw new Error(res.status === 404 ? 'Employee not found' : 'Failed to load');
        const data = await res.json();
        if (!cancelled) setForm(data);
      } catch (err) {
        if (!cancelled) setError(err.message);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [id]);

  async function onSubmit(e) {
    e.preventDefault();
    setBusy(true);
    setError('');
    try {
      await updateEmployee(id, {
        name: form.name,
        email: form.email,
        department: form.department,
        position: form.position,
        salary: Number(form.salary),
      });
      router.push(`/employees/${id}`);
      router.refresh();
    } catch (err) {
      setError(err.message);
      setBusy(false);
    }
  }

  if (error && !form) {
    return (
      <main>
        <div className="error">{error}</div>
        <p style={{ marginTop: '1rem' }}>
          <Link href="/employees">← Back</Link>
        </p>
      </main>
    );
  }

  if (!form) {
    return (
      <div className="panel loading">
        <p>Loading employee…</p>
        <div className="skeleton" style={{ width: '50%' }} />
      </div>
    );
  }

  function setField(key, value) {
    setForm((prev) => ({ ...prev, [key]: value }));
  }

  return (
    <main>
      <h1>Edit employee</h1>
      <p className="sub">PUT /api/employees/{id}</p>

      <div className="panel">
        <form className="form" onSubmit={onSubmit}>
          <label>
            Name
            <input
              value={form.name}
              onChange={(e) => setField('name', e.target.value)}
              required
            />
          </label>
          <label>
            Email
            <input
              type="email"
              value={form.email}
              onChange={(e) => setField('email', e.target.value)}
              required
            />
          </label>
          <label>
            Department
            <input
              value={form.department}
              onChange={(e) => setField('department', e.target.value)}
              required
            />
          </label>
          <label>
            Position
            <input
              value={form.position}
              onChange={(e) => setField('position', e.target.value)}
              required
            />
          </label>
          <label>
            Salary (₹)
            <input
              type="number"
              min={1}
              value={form.salary}
              onChange={(e) => setField('salary', e.target.value)}
              required
            />
          </label>

          {error && <div className="error">{error}</div>}

          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button className="btn btn-primary" type="submit" disabled={busy}>
              {busy ? 'Saving…' : 'Update'}
            </button>
            <Link href={`/employees/${id}`} className="btn btn-ghost">
              Cancel
            </Link>
          </div>
        </form>
      </div>
    </main>
  );
}
