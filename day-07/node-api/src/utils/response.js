function ok(res, data, status = 200) {
  return res.status(status).json(data);
}

function created(res, data) {
  return res.status(201).json(data);
}

function noContent(res) {
  return res.status(204).send();
}

module.exports = { ok, created, noContent };
