/** In-memory data store — seeded from day-07 employee dataset */
const fs = require('fs');
const path = require('path');

const DATA_FILE = path.join(__dirname, '../../data/employees.json');

function loadSeed() {
  try {
    const raw = fs.readFileSync(DATA_FILE, 'utf8');
    const parsed = JSON.parse(raw);
    if (Array.isArray(parsed) && parsed.length) return parsed.map((e) => ({ ...e }));
  } catch {
    /* fall through */
  }
  return [
    { id: 1, name: 'Asha Patil', email: 'asha@example.com', department: 'Engineering', position: 'Developer', salary: 65000 },
    { id: 2, name: 'Ravi Shah', email: 'ravi@example.com', department: 'HR', position: 'Executive', salary: 48000 },
    { id: 3, name: 'Neha Joshi', email: 'neha@example.com', department: 'Engineering', position: 'QA Engineer', salary: 58000 },
  ];
}

let employees = loadSeed();
let nextId = employees.reduce((m, e) => Math.max(m, e.id), 0) + 1;

module.exports = {
  getAll: () => [...employees],
  getById: (id) => employees.find((e) => e.id === Number(id)) || null,
  insert: (data) => {
    const employee = { id: nextId++, ...data };
    employees.push(employee);
    return employee;
  },
  update: (id, data) => {
    const index = employees.findIndex((e) => e.id === Number(id));
    if (index < 0) return null;
    employees[index] = { ...employees[index], ...data, id: Number(id) };
    return employees[index];
  },
  remove: (id) => {
    const index = employees.findIndex((e) => e.id === Number(id));
    if (index < 0) return false;
    employees.splice(index, 1);
    return true;
  },
};
