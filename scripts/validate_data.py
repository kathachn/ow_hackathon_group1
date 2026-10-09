"""Validate the versioned input and output artifacts; standard library only."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CITIES = ("berlin", "frankfurt", "muenchen")


def validate():
    summary = {}
    for city in CITIES:
        tables = {}
        for kind in ("grid", "scored", "pois", "portfolio"):
            path = DATA / f"{city}_{kind}.csv"
            with path.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                columns = reader.fieldnames or []
                expected = {"lat", "lon"} if kind == "pois" else {"h3"}
                assert expected.issubset(columns), f"{path}: missing {expected - set(columns)}"
                rows = list(reader)
            assert rows, f"{path}: empty"
            if kind in ("grid", "scored"):
                ids = [r["h3"] for r in rows]
                assert len(ids) == len(set(ids)), f"{path}: duplicate H3 cells"
            tables[kind] = len(rows)
        assert tables["grid"] == tables["scored"], f"{city}: grid/scored count mismatch"
        for kind in ("pca", "plausibilitaet"):
            with (DATA / f"{city}_{kind}.json").open(encoding="utf-8") as handle:
                assert isinstance(json.load(handle), dict)
        summary[city] = tables
    with (DATA / "luecke_modell.json").open(encoding="utf-8") as handle:
        assert isinstance(json.load(handle), dict)
    return summary

if __name__ == "__main__":
    for city, tables in validate().items():
        print(city, tables)
    print("PASS: versioned data artifacts are structurally consistent")
