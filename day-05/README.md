# Day 05 — JavaScript Employee Dashboard

## Project overview
A responsive employee-management dashboard built with HTML, CSS, and vanilla JavaScript. It loads employee records asynchronously from local JSON and supports complete CRUD-style interactions in the browser.

## Features
- List employee records and dashboard metrics
- Search by name, email, department, or position
- Filter by department and sort by name, salary, or ID
- View a detailed employee dialog
- Add, edit, and delete employees
- Validate mandatory fields and salary
- Persist changes in browser `localStorage`
- Show loading, empty, success, and error states

## Stack
HTML5, CSS3, JavaScript ES6+, Fetch API, JSON, localStorage.

## Run
Because the project uses `fetch`, run it with VS Code **Live Server** or another local server:
```bash
cd employee-dashboard
python -m http.server 5500
```
Then open `http://localhost:5500` in a browser.

## Project structure
```text
day-05/
├── javascript/
│   ├── exercises.js
│   └── array-methods.js
├── employee-dashboard/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── employees.json
└── README.md
```

## Technical decisions
`fetch` and `async/await` load initial JSON data. `map`, `filter`, `find`, `sort`, and `reduce` implement display, searching, details, ordering, and metrics. A single `render()` function updates the dashboard after each operation. `localStorage` makes changes remain after refresh without a backend.

## Challenges and solutions
- Local JSON cannot reliably be fetched using `file://`: use a local server.
- UI could become stale after CRUD actions: call `render()` after every state change.
- Invalid input: validate name, email, department, position, and positive salary before saving.

## Future improvements
Replace local storage with a REST API/database, add authentication, pagination, unit tests, and server-side validation.
