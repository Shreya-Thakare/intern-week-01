# Day 10 — Final Project

## Deliverables
```
day-10/
└── final-project/
    ├── frontend/          # Smart Facility Management Dashboard
    ├── backend/           # FastAPI hygiene risk API
    ├── database/          # SQL schema
    ├── ml/                # Training + saved model
    ├── angular-module/    # Functional Angular page → /predict
    └── README.md
```

## Run ML API
```bash
cd final-project/ml && python train.py
cd ../backend && python main.py
```

## Run frontend
Open `final-project/frontend/index.html` in a browser (API on :8000).

## Run Angular module
```bash
cd final-project/angular-module
npm install && npm start
```

## Presentation
Use `final-project/presentation-outline.md` for the 10–15 minute final presentation.
