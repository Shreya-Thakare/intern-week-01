# Day 7 — Next.js + Node.js API

Minimal full-stack employee app ready for a Git repo.

## Upload these files only

```text
day-07/
├── .gitignore
├── README.md
├── visualization.html          # works without npm
├── node-api/
│   ├── package.json
│   ├── data/employees.json
│   └── src/
│       ├── server.js
│       ├── routes/
│       ├── controllers/
│       ├── services/
│       ├── models/
│       ├── middleware/
│       └── utils/
└── nextjs-app/
    ├── package.json
    ├── .env.local.example
    ├── lib/api.js
    ├── lib/stats.js
    └── app/                    # pages, charts, CSS
```

**Never commit:** `node_modules/`, `.next/`, `.env.local`

After clone:

```bash
cd node-api && npm install && npm start
cd nextjs-app && npm install && npm run dev
```

Quick demo: open `visualization.html` in a browser.

## API

| Method | Path |
|--------|------|
| GET, POST | `/api/employees` |
| GET, PUT, DELETE | `/api/employees/:id` |

Dataset: `node-api/data/employees.json` (12 employees). Charts on `/employees`.
