const $ = (selector) => document.querySelector(selector);
const state = { employees: [], query: '', department: '', sort: 'name-asc' };

const money = (value) =>
  new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(value);

const setMessage = (text = '', isError = false) => {
  const el = $('#message');
  el.textContent = text;
  el.className = isError ? 'error' : '';
};

async function loadEmployees() {
  try {
    const saved = localStorage.getItem('day5Employees');
    state.employees = saved
      ? JSON.parse(saved)
      : await (await fetch('employees.json')).json();
    render();
  } catch (error) {
    setMessage(`Could not load employee data: ${error.message}`, true);
  }
}

function persist() {
  localStorage.setItem('day5Employees', JSON.stringify(state.employees));
}

function visibleEmployees() {
  const q = state.query.toLowerCase();
  const list = state.employees
    .filter((e) => !state.department || e.department === state.department)
    .filter((e) =>
      [e.name, e.email, e.department, e.position].some((v) =>
        String(v).toLowerCase().includes(q)
      )
    );

  return [...list].sort((a, b) => {
    if (state.sort === 'salary-desc') return b.salary - a.salary;
    if (state.sort === 'salary-asc') return a.salary - b.salary;
    if (state.sort === 'id-desc') return b.id - a.id;
    return a.name.localeCompare(b.name);
  });
}

function render() {
  const departments = [...new Set(state.employees.map((e) => e.department))].sort();
  $('#departmentFilter').innerHTML =
    '<option value="">All departments</option>' +
    departments
      .map(
        (d) =>
          `<option value="${d}" ${d === state.department ? 'selected' : ''}>${d}</option>`
      )
      .join('');

  $('#totalEmployees').textContent = state.employees.length;
  $('#departmentCount').textContent = departments.length;
  const avg =
    state.employees.reduce((sum, e) => sum + Number(e.salary), 0) /
    (state.employees.length || 1);
  $('#averageSalary').textContent = money(avg);

  const shown = visibleEmployees();
  $('#employeeRows').innerHTML = shown.length
    ? shown
        .map(
          (e) => `<tr>
      <td>
        <strong>${e.name}</strong>
        <div class="sub">${e.email}</div>
      </td>
      <td><span class="dept-pill">${e.department}</span></td>
      <td>${e.position}</td>
      <td><strong>${money(e.salary)}</strong></td>
      <td class="actions">
        <button type="button" class="sm" data-action="details" data-id="${e.id}">Details</button>
        <button type="button" class="sm" data-action="edit" data-id="${e.id}">Edit</button>
        <button type="button" class="sm danger" data-action="delete" data-id="${e.id}">Delete</button>
      </td>
    </tr>`
        )
        .join('')
    : '<tr><td colspan="5" style="color:var(--muted);padding:1.25rem 0.55rem">No employees match your search.</td></tr>';
}

function openForm(employee = null) {
  $('#employeeForm').reset();
  $('#employeeId').value = employee?.id || '';
  $('#formTitle').textContent = employee ? 'Edit employee' : 'Add employee';
  ['name', 'email', 'department', 'position', 'salary'].forEach((k) => {
    $('#' + k).value = employee?.[k] ?? '';
  });
  $('#formError').textContent = '';
  $('#employeeDialog').showModal();
}

function saveEmployee(event) {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(event.currentTarget));
  const employee = {
    id: Number(data.employeeId) || Date.now(),
    name: String(data.name || '').trim(),
    email: String(data.email || '').trim(),
    department: String(data.department || '').trim(),
    position: String(data.position || '').trim(),
    salary: Number(data.salary),
  };

  if (
    Object.values(employee).some((v) => v === '' || Number.isNaN(v)) ||
    employee.salary <= 0
  ) {
    $('#formError').textContent = 'Enter all fields and a positive salary.';
    return;
  }

  const index = state.employees.findIndex((e) => e.id === employee.id);
  if (index >= 0) state.employees[index] = employee;
  else state.employees.push(employee);

  persist();
  $('#employeeDialog').close();
  setMessage('Employee saved successfully.');
  render();
}

function details(employee) {
  $('#detailsContent').innerHTML = `
    <h2>${employee.name}</h2>
    <p><b>Email</b> ${employee.email}</p>
    <p><b>Department</b> ${employee.department}</p>
    <p><b>Position</b> ${employee.position}</p>
    <p><b>Salary</b> ${money(employee.salary)}</p>
  `;
  $('#detailsDialog').showModal();
}

$('#addButton').onclick = () => openForm();
$('#closeDialog').onclick = $('#cancelButton').onclick = () =>
  $('#employeeDialog').close();
$('#closeDetails').onclick = () => $('#detailsDialog').close();
$('#employeeForm').onsubmit = saveEmployee;
$('#searchInput').oninput = (e) => {
  state.query = e.target.value;
  render();
};
$('#departmentFilter').onchange = (e) => {
  state.department = e.target.value;
  render();
};
$('#sortSelect').onchange = (e) => {
  state.sort = e.target.value;
  render();
};

$('#employeeRows').onclick = (e) => {
  const b = e.target.closest('button[data-action]');
  if (!b) return;
  const employee = state.employees.find((x) => x.id === Number(b.dataset.id));
  if (!employee) return;
  if (b.dataset.action === 'details') details(employee);
  if (b.dataset.action === 'edit') openForm(employee);
  if (b.dataset.action === 'delete' && confirm(`Delete ${employee.name}?`)) {
    state.employees = state.employees.filter((x) => x.id !== employee.id);
    persist();
    setMessage('Employee deleted.');
    render();
  }
};

loadEmployees();
