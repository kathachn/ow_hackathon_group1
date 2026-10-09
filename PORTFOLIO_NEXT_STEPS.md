# Publication and recruitment checklist

## Before uploading

1. Preserve the existing GitHub `portfolio` branch as a backup or commit checkpoint.
2. Compare the supplied upgrade package against your current local `portfolio` branch.
3. Copy updated README, SETUP, data/README and the new `RESULTS.md`, `results_summary.csv`, `scripts/`, `tests/`, `.github/workflows/` files. Do not overwrite your newer application code if it differs.
4. Run `python scripts/validate_data.py` and `python -m unittest discover -s tests -v`.
5. Commit and push to **your own fork's `portfolio` branch**, not the original team repository.
6. Confirm GitHub Actions checks pass and the Streamlit application still works for all cities and tabs.
7. Verify the Streamlit Cloud deployment tracks `portfolio` and `app.py`; if the deployment tracks a different branch, update it deliberately.

## Additional work needed for a fully verified research-grade release

- Recompute model results from a clean environment and compare outputs within declared numerical tolerances.
- Add unit tests for scoring, spatial distance, candidate ranking, and portfolio selection functions.
- Add explicit temporal/spatial holdout evaluation and leakage checks.
- Capture a real dashboard screenshot with consent to use all visual assets; do not use a synthetic image as empirical evidence.
- Record Python version and lock resolved dependencies after a clean deployment succeeds.
- Verify data redistribution and visual-asset licenses; preserve the team attribution.
- Document your **own specific technical contributions** accurately.

## GitHub profile and CV

Pin `QuantRiskLab` and `ow_hackathon_group1`. Add the live demo URL to the repository About field. On the profile README, group the projects by quantitative finance / applied geospatial analytics. In the CV, label this project a *team project* and link the GitHub repository; add the live demo as a second link where space allows.
