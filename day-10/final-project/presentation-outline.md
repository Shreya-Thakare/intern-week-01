# Final Presentation — 10 to 15 Minutes

1. **Problem:** prioritize facilities that may need hygiene intervention.
2. **Stack:** HTML/CSS/JavaScript dashboard, FastAPI, Python/scikit-learn, SQL, Angular module.
3. **Architecture:** frontend sends validated data to FastAPI; API loads saved ML pipeline; database stores facility history.
4. **Demo:** train model, start API, submit form, explain returned risk probability.
5. **Difficult issue:** preventing data leakage—keep test data separate and use preprocessing inside a pipeline.
6. **Decision:** select model by F1 score because identifying high risk requires balance between precision and recall.
7. **Next week:** replace synthetic data with real data, add authentication, persistent storage, tests, monitoring and model retraining.
