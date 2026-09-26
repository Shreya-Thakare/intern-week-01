import Link from 'next/link';
import { fetchEmployees, money } from '../../lib/api';
import { buildStats } from '../../lib/stats';
import DeleteButton from './DeleteButton';
import Charts from './Charts';

export default async function EmployeesPage() {
  let employees = [];
  let error = '';

  try {
    employees = await fetchEmployees();
  } catch (err) {
    error = err.message;
  }

  const stats = buildStats(employees);

  return (
    <main>
      <div className="toolbar">
        <div>
          <h1>Employees</h1>
          <p className="sub">Dataset-backed dashboard · live from Node API</p>
        </div>
        <Link href="/employees/create" className="btn btn-primary">
          + Create employee
        </Link>
      </div>

      {error && (
        <div className="error" style={{ marginBottom: '1rem' }}>
          {error}
          <div style={{ marginTop: '0.35rem', fontSize: '0.85rem' }}>
            Start API: <code>cd node-api && npm start</code>
          </div>
        </div>
      )}

      {!error && (
        <section className="metrics">
          <div className="metric">
            <label>Total employees</label>
            <div className="value">{stats.total}</div>
            <div className="sub-line">In dataset</div>
          </div>
          <div className="metric">
            <label>Average salary</label>
            <div className="value">{money(stats.avg)}</div>
            <div className="sub-line">All departments</div>
          </div>
          <div className="metric">
            <label>Departments</label>
            <div className="value">{stats.deptStats.length}</div>
            <div className="sub-line">Unique teams</div>
          </div>
          <div className="metric">
            <label>Highest salary</label>
            <div className="value">{money(stats.max)}</div>
            <div className="sub-line">{stats.top ? stats.top.name : '—'}</div>
          </div>
        </section>
      )}

      {!error && stats.total > 0 && (
        <section className="panel" style={{ marginBottom: '1.15rem' }}>
          <div className="panel-head">
            <h2>Dataset visualization</h2>
            <span className="tag">From API data</span>
          </div>
          <Charts stats={stats} />
        </section>
      )}

      <div className="panel">
        <div className="panel-head">
          <h2>Employee roster</h2>
          <span className="tag">{employees.length} records</span>
        </div>
        {!error && employees.length === 0 && (
          <p className="muted">No employees yet. Create the first one.</p>
        )}
        {employees.length > 0 && (
          <div style={{ overflowX: 'auto' }}>
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
                {employees.map((e) => (
                  <tr key={e.id}>
                    <td>
                      <Link href={`/employees/${e.id}`}>
                        <strong>{e.name}</strong>
                      </Link>
                      <div style={{ fontSize: '0.75rem', color: 'var(--dim)' }}>{e.email}</div>
                    </td>
                    <td>{e.department}</td>
                    <td>{e.position}</td>
                    <td>{money(e.salary)}</td>
                    <td>
                      <div className="row-actions">
                        <Link href={`/employees/${e.id}`} className="btn btn-ghost btn-sm">
                          View
                        </Link>
                        <Link href={`/employees/${e.id}/edit`} className="btn btn-ghost btn-sm">
                          Edit
                        </Link>
                        <DeleteButton id={e.id} name={e.name} />
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </main>
  );
}
