"""
Zero-dependency Day 10 prediction API.
Works without fastapi/sklearn if packages are missing.

  python run_simple_api.py
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import json

PORT = 8000
MODEL_PATH = Path(__file__).resolve().parents[1] / "ml" / "hygiene_model.joblib"


def rule_predict(d):
    cleanliness = float(d.get("cleanliness_score", 5))
    odor = float(d.get("odor_score", 5))
    waste = float(d.get("waste_level", 5))
    complaints = float(d.get("complaints", 0))
    footfall = float(d.get("footfall", 0))
    hours = float(d.get("hours_since_cleaning", 0))
    score = (
        (10 - cleanliness) * 0.22
        + odor * 0.18
        + waste * 0.18
        + min(complaints, 12) * 0.12
        + min(hours / 48, 1) * 0.18
        + min(footfall / 800, 1) * 0.12
    )
    prob = max(0.0, min(1.0, score / 7.5))
    return {
        "hygiene_risk": "High" if prob >= 0.5 else "Low",
        "high_risk_probability": round(prob, 3),
        "mode": "rule-based",
    }


def ml_predict(d):
    try:
        import pandas as pd
        from joblib import load
    except ImportError:
        return None
    if not MODEL_PATH.exists():
        return None
    try:
        model = load(MODEL_PATH)
        x = dict(d)
        x["cleaning_delay_ratio"] = float(x["hours_since_cleaning"]) / (float(x["footfall"]) + 1) * 100
        prob = float(model.predict_proba(pd.DataFrame([x]))[0][1])
        return {
            "hygiene_risk": "High" if prob >= 0.5 else "Low",
            "high_risk_probability": round(prob, 3),
            "mode": "ml",
        }
    except Exception:
        return None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))

    def _send(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        if code != 204:
            self.wfile.write(body)

    def do_OPTIONS(self):
        self._send(204, {})

    def do_GET(self):
        if self.path.startswith("/health"):
            return self._send(
                200,
                {
                    "status": "ok",
                    "model_exists": MODEL_PATH.exists(),
                    "port": PORT,
                },
            )
        self._send(404, {"message": "Not found. Use GET /health or POST /predict"})

    def do_POST(self):
        if not self.path.startswith("/predict"):
            return self._send(404, {"message": "Not found"})
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw.decode() or "{}")
        except json.JSONDecodeError:
            return self._send(400, {"message": "Invalid JSON"})
        result = ml_predict(data) or rule_predict(data)
        self._send(200, result)


if __name__ == "__main__":
    print("Day 10 API running at http://localhost:%s" % PORT)
    print("  GET  /health")
    print("  POST /predict")
    print("Press Ctrl+C to stop")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
