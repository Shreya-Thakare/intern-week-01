# ERD

```text
Departments 1 ──── * Employees
Facilities  1 ──── * Inspections
Facilities  1 ──── * Complaints
```

Primary keys: `id`. Foreign keys: `employees.department_id`, `inspections.facility_id`, and `complaints.facility_id`.
