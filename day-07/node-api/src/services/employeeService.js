/**
 * Business logic layer between controllers and the data model.
 * Controllers must not talk to the model directly.
 */
const model = require('../models/employeeModel');

function listEmployees() {
  return model.getAll().sort((a, b) => a.id - b.id);
}

function getEmployee(id) {
  const employee = model.getById(id);
  if (!employee) {
    const err = new Error(`Employee ${id} not found`);
    err.status = 404;
    throw err;
  }
  return employee;
}

function createEmployee(payload) {
  const data = {
    name: String(payload.name).trim(),
    email: String(payload.email).trim(),
    department: String(payload.department).trim(),
    position: String(payload.position).trim(),
    salary: Number(payload.salary),
  };
  return model.insert(data);
}

function updateEmployee(id, payload) {
  getEmployee(id); // throws 404 if missing
  const data = {};
  if (payload.name !== undefined) data.name = String(payload.name).trim();
  if (payload.email !== undefined) data.email = String(payload.email).trim();
  if (payload.department !== undefined) data.department = String(payload.department).trim();
  if (payload.position !== undefined) data.position = String(payload.position).trim();
  if (payload.salary !== undefined) data.salary = Number(payload.salary);
  return model.update(id, data);
}

function deleteEmployee(id) {
  getEmployee(id);
  model.remove(id);
  return true;
}

module.exports = {
  listEmployees,
  getEmployee,
  createEmployee,
  updateEmployee,
  deleteEmployee,
};
