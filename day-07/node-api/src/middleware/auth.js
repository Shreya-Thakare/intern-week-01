/**
 * Authentication basics (Day 7 topic).
 * Demo mode: if AUTH_REQUIRED is not "true", requests pass through.
 * When enabled, expects header: Authorization: Bearer day7-secret
 */
function authOptional(req, res, next) {
  const required = process.env.AUTH_REQUIRED === 'true';
  if (!required) return next();

  const header = req.headers.authorization || '';
  const token = header.startsWith('Bearer ') ? header.slice(7) : '';
  const expected = process.env.API_TOKEN || 'day7-secret';

  if (!token || token !== expected) {
    return res.status(401).json({ message: 'Unauthorized. Provide Authorization: Bearer <token>' });
  }
  req.user = { role: 'admin' };
  next();
}

module.exports = authOptional;
