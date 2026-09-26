/** Shared API helpers for the Next.js app */
export const API_BASE =
  process.env.NEXT_PUBLIC_API_URL || 'http://localhost:4000/api';

export async function fetchEmployees() {
  const res = await fetch(`${API_BASE}/employees`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to load employees. Is the API running on port 4000?');
  return res.json();
}

export async function fetchEmployee(id) {
  const res = await fetch(`${API_BASE}/employees/${id}`, { cache: 'no-store' });
  if (!res.ok) {
    if (res.status === 404) return null;
    throw new Error('Failed to load employee');
  }
  return res.json();
}

export async function createEmployee(body) {
  const res = await fetch(`${API_BASE}/employees`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const msg = data.errors ? data.errors.join(', ') : data.message || 'Create failed';
    throw new Error(msg);
  }
  return data;
}

export async function updateEmployee(id, body) {
  const res = await fetch(`${API_BASE}/employees/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const msg = data.errors ? data.errors.join(', ') : data.message || 'Update failed';
    throw new Error(msg);
  }
  return data;
}

export async function deleteEmployee(id) {
  const res = await fetch(`${API_BASE}/employees/${id}`, { method: 'DELETE' });
  if (!res.ok && res.status !== 204) {
    const data = await res.json().catch(() => ({}));
    throw new Error(data.message || 'Delete failed');
  }
  return true;
}

export function money(n) {
  return '₹' + Number(n).toLocaleString('en-IN');
}
