# Day 9 — Angular + TypeScript + API Integration

## Project Overview
Facility Inspection Dashboard built with Angular (standalone components), Reactive Forms, RxJS/HttpClient and TypeScript models. Prepared as a stepping stone toward Ionic mobile development.

## Problem Statement
Give facility supervisors a single screen for metrics, facility search/sort, inspection history and recording new inspections against a REST API.

## Features
- Dashboard metrics: facility count, average cleanliness, needs-attention count
- Facility list with search and sort
- Facility details + inspection history
- Reactive form to add inspections (validated)
- HTTP client integration with offline fallback data
- TypeScript interfaces for Facility and Inspection

## Technology Stack
- Angular (standalone components)
- TypeScript
- RxJS / HttpClient
- Reactive Forms

## Architecture
```
day-09/
├── angular-app/
│   └── src/app/
│       ├── app.component.ts|html|css
│       ├── models/facility.model.ts
│       └── services/facility.service.ts
├── api-integration/
│   └── api-documentation.md
└── README.md
```

## Installation
```bash
cd angular-app
npm install
```

## Environment Variables
Optional: change `private api` in `facility.service.ts` (default `http://localhost:8000/api`).

## How to Run
```bash
# Optional: start Day 8 Laravel API on :8000
cd angular-app
npm start
```
Open http://localhost:4200

## Challenges Faced
- Keeping the dashboard usable when the Laravel API is offline
- Typing form status union consistently with the Inspection model

## Solutions
- Service-level `catchError` fallbacks for list/history/create
- Shared TypeScript interfaces in `models/`

## Future Improvements
- Route-based detail pages and guards
- Pagination and server-side filtering
- Ionic wrappers for mobile (future path)

## Standalone HTML dashboard (no Angular CLI)

Open this file for an immediate, effective facility inspection UI:

```text
day-09/index.html
```

Or serve it:

```bash
cd day-09
python -m http.server 5900
```

Open **http://localhost:5900**

Includes:
- Metrics (facilities, avg cleanliness, needs attention, inspections)
- Search / sort facility list
- Facility detail + reactive-style inspection form
- Cleanliness bar chart
- Inspection history
- Offline seed data (works without API)
