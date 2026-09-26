const service = require('../services/employeeService');
const { ok, created, noContent } = require('../utils/response');

async function list(req, res) {
  return ok(res, service.listEmployees());
}

async function getById(req, res) {
  return ok(res, service.getEmployee(req.params.id));
}

async function create(req, res) {
  return created(res, service.createEmployee(req.body));
}

async function update(req, res) {
  return ok(res, service.updateEmployee(req.params.id, req.body));
}

async function remove(req, res) {
  service.deleteEmployee(req.params.id);
  return noContent(res);
}

module.exports = { list, getById, create, update, remove };
