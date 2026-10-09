# Local setup and reproducibility

## Requirements

- Python 3.11 or newer is recommended as a starting point; exact version compatibility has not yet been validated.
- Dependencies are listed in `requirements.txt`.

## Run the dashboard using the included project data

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

The application reads precomputed results in `data/` where available. The included data may have source-specific attribution and redistribution obligations; consult `data/README.md` before publishing or redistributing it.

## Generate synthetic analysis results

```bash
python analyse.py --demo
```

The script writes synthetic outputs to `data/demo/`. The dashboard uses existing results from `data/` first and falls back to `data/demo/` when those files are absent. To demonstrate only synthetic outputs, use a separate working copy without the real precomputed outputs.

## Limitations

- The dashboard and end-to-end pipeline have **not yet been runtime-tested** in this portfolio revision.
- A successful Python syntax check is not proof of functional correctness.
- Dependency versions are not pinned to a lockfile, so this is not yet a fully reproducible environment.
- Live data acquisition in `datengrundlage.py` may depend on third-party services and their availability.
