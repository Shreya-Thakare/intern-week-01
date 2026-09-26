module.exports = (req, res, next) => {
  const { name, email, department, position, salary } = req.body || {};
  const errors = [];

  if (!name || !String(name).trim()) errors.push('name is required');
  if (!email || !String(email).trim()) errors.push('email is required');
  else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(email))) errors.push('email is invalid');
  if (!department || !String(department).trim()) errors.push('department is required');
  if (!position || !String(position).trim()) errors.push('position is required');
  if (salary === undefined || salary === null || Number(salary) <= 0) {
    errors.push('salary must be a positive number');
  }

  if (errors.length) {
    return res.status(400).json({ message: 'Validation failed', errors });
  }
  next();
};
