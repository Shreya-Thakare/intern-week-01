from pathlib import Path

import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from pydantic import BaseModel, Field

app = FastAPI(title="Hygiene Risk API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

model_path = Path(__file__).parents[1] / "ml" / "hygiene_model.joblib"


class FacilityFeatures(BaseModel):
    cleanliness_score: float = Field(ge=0, le=10)
    odor_score: float = Field(ge=0, le=10)
    waste_level: float = Field(ge=0, le=10)
    complaints: int = Field(ge=0)
    footfall: int = Field(ge=0)
    hours_since_cleaning: float = Field(ge=0)


@app.get("/health")
def health():
    return {"status": "ok", "model_exists": model_path.exists()}


@app.post("/predict")
def predict(data: FacilityFeatures):
    if not model_path.exists():
        raise HTTPException(503, "Train the model first: run ml/train.py")

    model = load(model_path)
    x = data.model_dump()
    x["cleaning_delay_ratio"] = x["hours_since_cleaning"] / (x["footfall"] + 1) * 100
    prob = float(model.predict_proba(pd.DataFrame([x]))[0][1])
    return {
        "hygiene_risk": "High" if prob >= 0.5 else "Low",
        "high_risk_probability": round(prob, 3),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

