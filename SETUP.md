# Installation, operation and verification

## Requirements

Recommended: Python 3.11 or 3.12. Python 3.13 was used successfully by the project maintainer on macOS, but cross-platform dependency resolution has not been independently certified.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/validate_data.py
python -m unittest discover -s tests -v
python -m streamlit run app.py
```

On Windows, activate using `.venv\Scripts\activate`. The local app is available at the address Streamlit prints (typically `http://localhost:8501`).

## Data flow

1. `datengrundlage.py` prepares geographical inputs using external data sources.
2. `analyse.py` computes scores, model diagnostics and portfolio outputs.
3. `app.py` displays saved artifacts in `data/`; if these are absent, it can fall back to `data/demo/`.
4. `scripts/validate_data.py` checks that saved CSV and JSON artifacts have the expected structural shape.

The included output files allow the dashboard to display existing results **without rerunning the external data collection or modelling pipeline**.

## Demo mode

`python analyse.py --demo` writes synthetic outputs to `data/demo/`. **Never present synthetic outputs as empirical results.** To use the demo fallback, isolate a copy of the repository without the corresponding real saved outputs.

## Reproducibility limitations

- Dependencies are specified by package name and some lower bounds, not a tested lockfile.
- External APIs, datasets and their availability can change.
- Structural tests do not validate statistical correctness or rerun the full model.
- See `RESULTS.md` for precise claims supported by versioned artifacts.
