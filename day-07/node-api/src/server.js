const express = require('express');
const cors = require('cors');
const employeeRoutes = require('./routes/employeeRoutes');
const errorHandler = require('./middleware/errorHandler');

const app = express();
const PORT = process.env.PORT || 4000;

app.use(cors());
app.use(express.json());

app.get('/health', (_req, res) => {
  res.json({
    status: 'ok',
    authRequired: process.env.AUTH_REQUIRED === 'true',
  });
});

app.use('/api/employees', employeeRoutes);
app.use(errorHandler);

app.listen(PORT, () => {
  console.log(`Employee API listening on http://localhost:${PORT}`);
  console.log(`Health: http://localhost:${PORT}/health`);
});
