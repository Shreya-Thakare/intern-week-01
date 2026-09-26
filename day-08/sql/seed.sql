USE facility_management;

INSERT INTO departments (name) VALUES
  ('Engineering'),
  ('HR'),
  ('Operations');

INSERT INTO employees (department_id, name, email, salary) VALUES
  (1, 'Asha Patil', 'asha@example.com', 65000),
  (2, 'Ravi Shah', 'ravi@example.com', 48000),
  (1, 'Neha Joshi', 'neha@example.com', 58000);

INSERT INTO facilities (name, location, cleanliness_score, water_availability) VALUES
  ('Central Washroom', 'Nagpur Central', 5.5, TRUE),
  ('Cafeteria', 'Dharampeth', 8.2, TRUE),
  ('Library Restroom', 'Sitabuldi', 6.8, FALSE);

INSERT INTO inspections (facility_id, inspection_date, cleanliness_score, odor_score, waste_level, status, remarks) VALUES
  (1, '2026-09-20', 5, 7, 6, 'Needs Attention', 'Cleaning needed'),
  (2, '2026-09-20', 8, 2, 2, 'Good', 'Maintained'),
  (3, '2026-09-21', 6, 4, 5, 'Needs Attention', 'Monitor odor');

INSERT INTO complaints (facility_id, description, status) VALUES
  (1, 'Bad odor reported', 'Open'),
  (1, 'Waste bin is full', 'In Progress'),
  (3, 'Water not available', 'Open');
