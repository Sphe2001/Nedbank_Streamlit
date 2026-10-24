# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
The primary user is the assignment marker (lecturer or tutor) assessing IDA117V Question 7. They open the app locally or at a Streamlit Community Cloud URL and work through the rubric: 7.1 working interface, 7.2 input/prediction/explanation, 7.3 validation and responsible use, 7.4 launch, deployment and demonstrations. Their job is to check quickly that every claim in the evidence is visible and works. The capacity-planning analyst is an implied framing at most; the app is not designed around them.

## Product Purpose
A Streamlit web app that serves the saved, unchanged optimised Random Forest classifier and sorts a customer's future transaction demand (November 2015–January 2016) into three classes: Low (0–49), Medium (50–199) or High (200+). Success means the marker can run the three valid demos and the one invalid demo, see a class, its probabilities and a short explanation, and confirm that validation and responsible-use safeguards are real.

## Positioning
It uses the notebook's saved champion pipeline (training-fitted imputation with missing-value flags, arcsinh transform, scaler, tuned Random Forest with 200 trees, max_features 1.0, depth 12, minimum leaf size 6) with no retraining. Every rubric item is backed by reproducible AppTest evidence (`evidence/test_results.json`).

## Operating Context
- Run locally with `python -m streamlit run streamlit_app.py` (http://localhost:8501) or deploy to Streamlit Community Cloud (not deployed yet; no public URL is claimed).
- Three input methods: Demonstration cases (synthetic), Upload/paste CSV (43-feature schema from the notebook, ≤1,000 rows, ≤2 MB), Manual entry (editable feature table seeded from templates).
- Outputs: predicted class metric, model probability, per-class probability table, explanation text, CSV download.
- Supporting documents: `README.md`, `Question_7_Evidence.md`, `feature_guidance.csv`.

## Capabilities and Constraints
- **Stay in Streamlit.** No framework rewrite. Visual work is limited to `.streamlit/config.toml`, light injected CSS and Streamlit layout primitives.
- **Keep `test_app.py` passing.** Widget keys (`input_mode`, `demo_case`, `predict_demo`, `pasted_csv`, `predict_upload`, `predict_manual`, `manual_profile`, `feature_csv`), the radio/selectbox option labels, the metric order (class first, probability second) and the error message text that the tests assert on must not change.
- Validation covers schema, nonnumeric/negative/fractional/infinite values, flag ranges, rolling-count consistency and rejection of extra columns (including identifiers).
- Python 3.12; pinned dependencies in `requirements.txt`.
- Terminology: "demand class", "Low/Medium/High", "model probability" (uncalibrated), "feature profile".
- Undecided: public deployment URL; reuse permission for publishing the model.

## Brand Commitments
"Nedbank" is only where the dataset came from (Zindi Nedbank Transaction Volume Forecasting Challenge). The app must not use Nedbank branding or imply endorsement. The working title is the neutral "Banking demand forecast". Course identifier: IDA117V.

## Evidence on Hand
- `evidence/test_results.json`: 10 passing checks (Low 81.2%, Medium 85.6%, High 80.7%, invalid negative count, CSV path, missing feature, manual profile, rolling-count, identifier block, pipeline fidelity).
- `evidence/package_hashes.json`, `evidence/server_startup.json`.
- `examples/valid_features.csv`, `examples/invalid_features.csv` (synthetic).
- `artifacts/classification_pipeline.joblib`, `artifacts/feature_schema.json`.
- Absent and never to be invented: a live deployment URL, real customer records, calibrated probabilities, operational accuracy on current customers, measured service benefits.

## Product Principles
1. **Make the rubric legible.** A marker should be able to map each screen element to 7.1–7.4 without reading the code.
2. **Honest model claims.** Probabilities are uncalibrated, the data is historical (2015) and the thresholds are project assumptions. The interface must not overstate certainty or real-world validity. Disclaimer wording may be refined, but the substance stays.
3. **Privacy by default.** Synthetic inputs only, no identifiers accepted, processing in memory.
4. **Fidelity over flash.** The saved pipeline is the product. Never reimplement or bypass preprocessing.
5. **Evidence stays reproducible.** Any change keeps `python test_app.py` green.
