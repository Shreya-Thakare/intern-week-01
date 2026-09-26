const express = require('express');
const controller = require('../controllers/employeeController');
const validateEmployee = require('../middleware/validateEmployee');
const auth = require('../middleware/auth');
const asyncHandler = require('../utils/asyncHandler');

const router = express.Router();

router.use(auth);

router.get('/', asyncHandler(controller.list));
router.get('/:id', asyncHandler(controller.getById));
router.post('/', validateEmployee, asyncHandler(controller.create));
router.put('/:id', validateEmployee, asyncHandler(controller.update));
router.delete('/:id', asyncHandler(controller.remove));

module.exports = router;
