import Link from 'next/link';
import { notFound } from 'next/navigation';
import { fetchEmployee, money } from '../../../lib/api';
import DeleteButton from '../DeleteButton';

export default async function EmployeeDetailPage({ params }) {
  const { id } = await params;
  let employee = null;
  let error = '';

  try {
    employee = await fetchEmployee(id);
  } catch (err) {
    error = err.message;
  }

  if (!error && !employee) notFound();

  if (error) {
    return (
      <main>
        <div className="error">{error}</div>
        <p style={{ marginTop: '1rem' }}>
          <Link href="/employees">← Back to employees</Link>
        </p>
      </main>
    );
  }

  return (
    <main>
      <p className="sub">
        <Link href="/employees">← Employees</Link>
      </p>
      <h1>{employee.name}</h1>
      <p className="sub">GET /api/employees/{employee.id}</p>

      <div className="panel">
        <div className="detail-grid">
          <div>
            <span>Email</span>
            <strong>{employee.email}</strong>
          </div>
          <div>
            <span>Department</span>
            <strong>{employee.department}</strong>
          </div>
          <div>
            <span>Position</span>
            <strong>{employee.position}</strong>
          </div>
          <div>
            <span>Salary</span>
            <strong>{money(employee.salary)}</strong>
          </div>
          <div>
            <span>ID</span>
            <strong>#{employee.id}</strong>
          </div>
        </div>

        <div className="row-actions">
          <Link href={`/employees/${employee.id}/edit`} className="btn btn-primary">
            Edit
          </Link>
          <DeleteButton id={employee.id} name={employee.name} />
          <Link href="/employees" className="btn btn-ghost">
            Back
          </Link>
        </div>
      </div>
    </main>
  );
}
