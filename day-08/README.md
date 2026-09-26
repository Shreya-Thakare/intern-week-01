# Day 8 — Database + Laravel

## Project Overview
Relational database design for facility management plus a Laravel REST CRUD API for Facilities, Inspections and Complaints.

## Problem Statement
Model users/departments/employees/facilities/inspections/complaints with proper relationships, write analytical SQL, and implement Laravel API endpoints following Request → Route → Controller → Model → Database → Response.

## Features
- SQL schema with primary/foreign keys and indexes
- Seed data and analytical queries (avg salary, poor facilities, complaint counts, inspection history)
- Laravel Eloquent models with relationships
- Full CRUD controllers with validation for Facilities, Inspections, Complaints
- Migration file for all tables
- Nested route: `GET /api/facilities/{id}/inspections`

## Technology Stack
- MySQL / MariaDB compatible SQL
- Laravel (Eloquent ORM, Form Request validation style)
- PHP 8+

## Architecture
```
day-08/
├── sql/
│   ├── schema.sql
│   ├── seed.sql
│   └── queries.sql
├── database/
│   └── erd.md
└── laravel-api/
    ├── app/Models/
    ├── app/Http/Controllers/
    ├── database/migrations/
    └── routes/api.php
```

## Database Design
- departments 1—* employees
- facilities 1—* inspections
- facilities 1—* complaints

See `database/erd.md` and `sql/schema.sql`.

## API Documentation
| Method | Path | Description |
|--------|------|-------------|
| GET/POST | /api/facilities | List / create |
| GET/PUT/DELETE | /api/facilities/{id} | Read / update / delete |
| GET/POST | /api/inspections | List / create |
| GET/PUT/DELETE | /api/inspections/{id} | Read / update / delete |
| GET/POST | /api/complaints | List / create |
| GET/PUT/DELETE | /api/complaints/{id} | Read / update / delete |
| GET | /api/facilities/{id}/inspections | Inspection history |

## Installation
```bash
# SQL
mysql -u root -p < sql/schema.sql
mysql -u root -p < sql/seed.sql

# Laravel (drop these files into a fresh `laravel new` app, or)
cd laravel-api
# composer install  (requires full Laravel skeleton)
php artisan migrate
php artisan serve
```

## How to Run (no MySQL)

```bash
cd day-08
python run_sqlite_demo.py
```

## How to Run (MySQL / Laravel)
1. Import SQL schema + seed.
2. Place models/controllers/routes into a Laravel project and run `php artisan serve`.
3. Test with: `curl http://localhost:8000/api/facilities`

## Challenges Faced
- Mapping ENUM status values consistently between SQL and validation rules
- Keeping controllers thin while still validating every write

## Solutions
- Shared validation rules in each controller method
- Eloquent relationships for nested JSON responses

## Future Improvements
- Form Request classes
- API authentication (Sanctum)
- Policy-based authorization
