# Global Cost of Living Comparator

A lightweight Streamlit dashboard to compare cost-of-living indices across 75+ major cities worldwide. It uses a hardcoded dataset and provides interactive filters, summary metrics, and Plotly charts.

## Features
- Compare cities by region, choose specific cities, and pick a primary metric for ranking.
- Interactive bar and scatter charts (Plotly) and a data table view.

## Requirements
- Python 3.8+
- Packages listed in `requirements.txt` (Streamlit, pandas, plotly).

## Run locally
1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

The app will open in your browser at http://localhost:8501 by default.

## Deploy to Streamlit Community Cloud
1. Push your repository to GitHub and ensure `app.py` and `requirements.txt` are at the repo root.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, choose the repository and branch, and set the main file to `app.py`.
4. Click **Deploy** — Streamlit will install packages from `requirements.txt` and launch the app.

Notes:
- If you need private environment variables or API keys, add them under the app's **Settings → Secrets** in the Streamlit dashboard.
- If the app requires a different Python version, set `runtime.txt` or use Streamlit's advanced settings documented on their site.

## Troubleshooting
- If Plotly charts don't render correctly, ensure `plotly` is installed and up-to-date.
- If Streamlit fails to start, check for missing dependencies or Python version mismatches.

---
Created for local demos and workshops. Feel free to adapt the data source to load CSVs or external APIs.
# streamlit-workshop
The repository for workshop - Data Apps Made Easy: An Introduction to Streamlit.
