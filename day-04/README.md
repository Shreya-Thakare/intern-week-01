# Day 04 — Facility Hygiene Risk Prediction

## Project overview
This supervised machine-learning project predicts whether a facility has **High** or **Low** hygiene risk. It follows the required workflow: dataset → cleaning → EDA → feature engineering → train/test split → model training → prediction → evaluation.

## Problem statement
Manual inspection records can be difficult to prioritize. This project classifies hygiene risk using `cleanliness_score`, `odor_score`, `waste_level`, `complaints`, `footfall`, and `hours_since_cleaning`.

## Features and label
| Item | Details |
|---|---|
| Input features | cleanliness score, odor score, waste level, complaints, footfall, hours since cleaning |
| Engineered feature | cleaning-delay ratio = hours since cleaning / (footfall + 1) × 100 |
| Label | `hygiene_risk`: High or Low |
| Algorithms compared | Logistic Regression and Random Forest |
| Test split | 25%, stratified, `random_state=42` |
| Selection measure | F1 score, appropriate because missing high-risk facilities is important |

## Folder structure
```text
day-04/
├── dataset/facility_hygiene_raw.csv
├── preprocessing/facility_hygiene_cleaned.csv
├── models/best_hygiene_risk_model.joblib
├── evaluation/
├── predictions/test_predictions.csv
├── visualizations/
├── run_project.py
├── requirements.txt
└── README.md
```

## Installation and run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_project.py
```

## Cleaning and leakage control
- Removes duplicate facility IDs.
- Converts non-numeric values to missing values.
- Replaces scores outside 0–10 and negative numeric values with missing values.
- Uses median imputation inside the model pipeline, fitted only on training data.
- Keeps the test set separate until final evaluation.

## Outputs
Run the script to regenerate the cleaned data, two EDA charts, comparison table, confusion matrices, classification reports, model file, and test predictions. See `evaluation/selected_model.txt` for the selected model and measured F1 score.

## Challenges and solutions
| Challenge | Solution |
|---|---|
| Missing/invalid values | Validate ranges, then median imputation |
| Duplicate records | Deduplicate by facility ID |
| Risk-class evaluation | Compare precision, recall and F1—not accuracy alone |
| Potential overfitting | Use a held-out stratified test set and constrain Random Forest depth |

## Future improvements
Use real inspection data, define risk labels with domain experts, tune hyperparameters with cross-validation, track model drift, add fairness checks, and expose validated predictions through an API. This model is for prioritization and must not replace human safety inspection.
