# Day 6 — TypeScript + React

## Project Overview
Build a typed Employee Management Dashboard with React and TypeScript, covering components, hooks, forms, validation, and an API-shaped data layer.

## Problem Statement
Convert the Day 5 employee application concepts into a maintainable TypeScript + React SPA with metrics, list/search/filter/sort/details, and full CRUD.

## Features
- Dashboard metrics: total employees, average salary, department count
- List, search, department filter, multi-key sort (asc/desc)
- Employee details modal
- Add / edit / delete with form validation (required fields + email)
- LocalStorage persistence behind async API-style helpers
- TypeScript interfaces, enums, generics, type guards in `typescript/`

## Technology Stack
- TypeScript
- React 18 (hooks: useState, useEffect, useMemo)
- Vite

## Architecture
```
day-06/
├── typescript/          # Types, interfaces, exercises
│   ├── employee-types.ts
│   └── type-exercises.ts
├── react-app/           # Vite + React + TS dashboard
│   └── src/App.tsx
└── README.md
```

## Installation
```bash
cd react-app
npm install
```

## Environment Variables
None required (data persists in browser localStorage).

## How to Run
```bash
cd react-app
npm run dev
```
Open the printed local URL (usually http://localhost:5173).

TypeScript exercises (optional):
```bash
cd typescript
npx tsc --noEmit employee-types.ts type-exercises.ts
```

## Challenges Faced
- Keeping UI state and persisted data in sync without a real backend
- Typing form events and optional edit mode cleanly

## Solutions
- Async `apiList` / `apiSave` helpers mirror REST client shape
- Single `Employee` interface shared conceptually with the typescript exercises folder

## Future Improvements
- Wire to Day 7 Node API instead of localStorage
- Extract table and form into reusable components
- Add unit tests with React Testing Library

## Standalone visualization (no npm)

Open this file in a browser for a full dark-theme dashboard with accurate live charts:

```text
day-06/index.html
```

Features:
- Metrics: total, average salary, departments, highest salary
- Charts: average salary by department, headcount donut, salary bands
- List / search / filter / sort / details / add / edit / delete
- Data persists in localStorage

Or:
```bash
cd day-06
python -m http.server 5600
```
Then open http://localhost:5600
