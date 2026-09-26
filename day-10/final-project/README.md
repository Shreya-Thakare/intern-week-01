# Day 10 — Final Project: Smart Hygiene Risk Prediction System

## Project Overview
End-to-end system that predicts facility hygiene risk from inspection-style features, exposes predictions through a REST API, and surfaces them in a web dashboard plus a dedicated Angular module.

## Problem Statement
Facility supervisors need an early-warning signal for washrooms and public facilities that are likely high-risk (poor cleanliness, odor, waste, high footfall, delayed cleaning, repeated complaints) so inspections can be prioritised.

## Features
- ML pipeline: training, evaluation, model persistence (`ml/`)
- FastAPI prediction API with input validation (`backend/`)
- Responsive facility management dashboard (`frontend/`)
- Functional Angular module connected to `/predict` (`angular-module/`)
- SQL schema for facilities, inspections, complaints (`database/`)

## Technology Stack
- Python, scikit-learn / joblib, FastAPI, Pandas
- HTML/CSS/JS dashboard
- Angular + TypeScript + HttpClient
- MySQL-compatible SQL schema

## Architecture
```text
Angular module / Frontend dashboard
            │  POST /predict
            ▼
     FastAPI backend  ── loads ──► ml/hygiene_model.joblib
            │
            └── database/schema.sql (facilities, inspections, complaints)
```

## Database Design
See `database/schema.sql`:
- `facilities`
- `inspections` (FK → facilities)
- `complaints` (FK → facilities)

## API Documentation
### GET /health
Returns API + model availability.

### POST /predict
```json
{
  "cleanliness_score": 5,
  "odor_score": 7,
  "waste_level": 6,
  "complaints": 4,
  "footfall": 350,
  "hours_since_cleaning": 24
}
```
Response:
```json
{ "hygiene_risk": "High", "high_risk_probability": 0.82 }
```

## Installation
```bash
# ML + API
cd ml && pip install -r requirements.txt && python train.py
cd ../backend && pip install -r requirements.txt

# Angular module (optional demo)
cd ../angular-module && npm install
```

## Environment Variables
None required. API defaults to `http://localhost:8000`.

## How to Run
```bash
# 1. Train model (once)
cd ml && python train.py

# 2. Start API
cd backend && python main.py

# 3. Open dashboard
open frontend/index.html
# or serve statically: python -m http.server 5500 --directory frontend

# 4. Angular module
cd angular-module && npm start
```

## Challenges Faced
- Keeping the UI useful when the model file is missing
- Aligning feature names between training script and API payload
- Providing both a lightweight HTML dashboard and a real Angular page

## Solutions
- API returns HTTP 503 with a clear message if the model is not trained
- Shared feature set + engineered `cleaning_delay_ratio`
- Angular module uses the same `/predict` contract as the HTML form

## Future Improvements
- Persist predictions and inspections to the SQL database
- Authentication and role-based access
- Cross-validation, drift monitoring, and fairness checks
- Promote the Angular module into a full Ionic mobile app

## Presentation outline
See `presentation-outline.md`.
