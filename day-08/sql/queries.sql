-- Employees per department
SELECT d.name AS department, e.name, e.salary
FROM departments d
JOIN employees e ON e.department_id = d.id
ORDER BY d.name, e.name;

-- Average salary
SELECT AVG(salary) AS average_salary FROM employees;

-- Highest-paid employee
SELECT name, salary FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Facilities needing attention / poor condition
SELECT f.name, f.location, i.status, i.inspection_date
FROM facilities f
JOIN inspections i ON i.facility_id = f.id
WHERE i.status IN ('Needs Attention', 'Poor')
ORDER BY i.inspection_date DESC;

-- Complaint counts per facility
SELECT f.name, COUNT(c.id) AS complaint_count
FROM facilities f
LEFT JOIN complaints c ON c.facility_id = f.id
GROUP BY f.id, f.name
ORDER BY complaint_count DESC;

-- Inspection history for every facility
SELECT f.name, i.inspection_date, i.cleanliness_score, i.odor_score, i.waste_level, i.status
FROM facilities f
JOIN inspections i ON i.facility_id = f.id
ORDER BY f.name, i.inspection_date DESC;

-- Transaction example
START TRANSACTION;
UPDATE complaints SET status = 'Resolved' WHERE id = 1;
COMMIT;
