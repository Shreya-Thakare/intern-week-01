import { useEffect, useMemo, useState, FormEvent } from 'react';

interface Employee {
  id: number;
  name: string;
  email: string;
  department: string;
  position: string;
  salary: number;
}

type SortKey = 'name' | 'department' | 'salary' | 'id';

const STORAGE_KEY = 'day06-employees';

const seed: Employee[] = [
  { id: 1, name: 'Asha Patil', email: 'asha@example.com', department: 'Engineering', position: 'Developer', salary: 65000 },
  { id: 2, name: 'Ravi Shah', email: 'ravi@example.com', department: 'HR', position: 'Executive', salary: 48000 },
  { id: 3, name: 'Neha Joshi', email: 'neha@example.com', department: 'Engineering', position: 'QA Engineer', salary: 58000 },
  { id: 4, name: 'Karan Mehta', email: 'karan@example.com', department: 'Finance', position: 'Analyst', salary: 52000 },
];

function loadEmployees(): Employee[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw) as Employee[];
      if (Array.isArray(parsed) && parsed.length) return parsed;
    }
  } catch {
    /* ignore */
  }
  return seed;
}

function persist(employees: Employee[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(employees));
}

/** Simulated API layer — same shape as a real REST client */
async function apiList(): Promise<Employee[]> {
  await new Promise((r) => setTimeout(r, 150));
  return loadEmployees();
}

async function apiSave(all: Employee[]): Promise<void> {
  await new Promise((r) => setTimeout(r, 80));
  persist(all);
}

export default function App() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [query, setQuery] = useState('');
  const [department, setDepartment] = useState('');
  const [sortKey, setSortKey] = useState<SortKey>('name');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc');
  const [editing, setEditing] = useState<Employee | null>(null);
  const [details, setDetails] = useState<Employee | null>(null);
  const [formError, setFormError] = useState('');

  useEffect(() => {
    apiList()
      .then(setEmployees)
      .catch(() => setError('Failed to load employees'))
      .finally(() => setLoading(false));
  }, []);

  const departments = useMemo(
    () => [...new Set(employees.map((e) => e.department))].sort(),
    [employees]
  );

  const shown = useMemo(() => {
    let list = employees.filter((e) => {
      const matchDept = !department || e.department === department;
      const q = query.trim().toLowerCase();
      const matchQ =
        !q ||
        e.name.toLowerCase().includes(q) ||
        e.department.toLowerCase().includes(q) ||
        e.position.toLowerCase().includes(q) ||
        e.email.toLowerCase().includes(q);
      return matchDept && matchQ;
    });
    list = [...list].sort((a, b) => {
      const av = a[sortKey];
      const bv = b[sortKey];
      if (av < bv) return sortDir === 'asc' ? -1 : 1;
      if (av > bv) return sortDir === 'asc' ? 1 : -1;
      return 0;
    });
    return list;
  }, [employees, query, department, sortKey, sortDir]);

  const avg = employees.length
    ? Math.round(employees.reduce((s, e) => s + e.salary, 0) / employees.length)
    : 0;

  async function commit(next: Employee[]) {
    setEmployees(next);
    await apiSave(next);
  }

  function openAdd() {
    setEditing({
      id: 0,
      name: '',
      email: '',
      department: '',
      position: '',
      salary: 0,
    });
    setFormError('');
  }

  function openEdit(e: Employee) {
    setEditing({ ...e });
    setFormError('');
  }

  async function save(ev: FormEvent<HTMLFormElement>) {
    ev.preventDefault();
    if (!editing) return;
    const f = new FormData(ev.currentTarget);
    const x: Employee = {
      id: editing.id || Date.now(),
      name: String(f.get('name') || '').trim(),
      email: String(f.get('email') || '').trim(),
      department: String(f.get('department') || '').trim(),
      position: String(f.get('position') || '').trim(),
      salary: Number(f.get('salary')),
    };
    if (!x.name || !x.email || !x.department || !x.position || !(x.salary > 0)) {
      setFormError('All fields are required and salary must be positive.');
      return;
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(x.email)) {
      setFormError('Enter a valid email address.');
      return;
    }
    const exists = employees.some((e) => e.id === x.id);
    const next = exists
      ? employees.map((e) => (e.id === x.id ? x : e))
      : [...employees, x];
    await commit(next);
    setEditing(null);
  }

  async function remove(e: Employee) {
    if (!confirm(`Delete ${e.name}?`)) return;
    await commit(employees.filter((x) => x.id !== e.id));
    if (details?.id === e.id) setDetails(null);
  }

  if (loading) return <main className="page"><p>Loading employees…</p></main>;
  if (error) return <main className="page"><p className="error">{error}</p></main>;

  return (
    <main className="page">
      <header className="header">
        <div>
          <small>DAY 06 • TYPESCRIPT + REACT</small>
          <h1>Employee Management Dashboard</h1>
        </div>
        <button type="button" onClick={openAdd}>
          + Add employee
        </button>
      </header>

      <section className="metrics">
        <div>
          <span>Total employees</span>
          <b>{employees.length}</b>
        </div>
        <div>
          <span>Average salary</span>
          <b>₹{avg.toLocaleString()}</b>
        </div>
        <div>
          <span>Departments</span>
          <b>{departments.length}</b>
        </div>
      </section>

      <section className="toolbar">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search name, dept, position, email"
        />
        <select value={department} onChange={(e) => setDepartment(e.target.value)}>
          <option value="">All departments</option>
          {departments.map((d) => (
            <option key={d} value={d}>
              {d}
            </option>
          ))}
        </select>
        <select value={sortKey} onChange={(e) => setSortKey(e.target.value as SortKey)}>
          <option value="name">Sort: Name</option>
          <option value="department">Sort: Department</option>
          <option value="salary">Sort: Salary</option>
          <option value="id">Sort: ID</option>
        </select>
        <button type="button" onClick={() => setSortDir((d) => (d === 'asc' ? 'desc' : 'asc'))}>
          {sortDir === 'asc' ? '↑ Asc' : '↓ Desc'}
        </button>
      </section>

      <section className="panel">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Department</th>
              <th>Position</th>
              <th>Salary</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {shown.map((e) => (
              <tr key={e.id}>
                <td>{e.name}</td>
                <td>{e.department}</td>
                <td>{e.position}</td>
                <td>₹{e.salary.toLocaleString()}</td>
                <td className="actions">
                  <button type="button" onClick={() => setDetails(e)}>
                    Details
                  </button>
                  <button type="button" onClick={() => openEdit(e)}>
                    Edit
                  </button>
                  <button type="button" className="danger" onClick={() => remove(e)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
            {!shown.length && (
              <tr>
                <td colSpan={5}>No employees match your filters.</td>
              </tr>
            )}
          </tbody>
        </table>
      </section>

      {editing && (
        <div className="modal">
          <form className="dialog" onSubmit={save}>
            <h2>{editing.id ? 'Edit employee' : 'Add employee'}</h2>
            <label>
              Name
              <input name="name" defaultValue={editing.name} required />
            </label>
            <label>
              Email
              <input name="email" type="email" defaultValue={editing.email} required />
            </label>
            <label>
              Department
              <input name="department" defaultValue={editing.department} required />
            </label>
            <label>
              Position
              <input name="position" defaultValue={editing.position} required />
            </label>
            <label>
              Salary
              <input name="salary" type="number" min={1} defaultValue={editing.salary || ''} required />
            </label>
            {formError && <p className="error">{formError}</p>}
            <div className="actions">
              <button type="button" onClick={() => setEditing(null)}>
                Cancel
              </button>
              <button type="submit">Save</button>
            </div>
          </form>
        </div>
      )}

      {details && (
        <div className="modal" onClick={() => setDetails(null)}>
          <div className="dialog" onClick={(e) => e.stopPropagation()}>
            <h2>{details.name}</h2>
            <p><b>Email:</b> {details.email}</p>
            <p><b>Department:</b> {details.department}</p>
            <p><b>Position:</b> {details.position}</p>
            <p><b>Salary:</b> ₹{details.salary.toLocaleString()}</p>
            <button type="button" onClick={() => setDetails(null)}>Close</button>
          </div>
        </div>
      )}
    </main>
  );
}
