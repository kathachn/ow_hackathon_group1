# Results and validation notes

The following values are extracted from **versioned outputs** in `data/`. They are not independent estimates or new model runs.

| City | H3 cells | OSM POIs | Selected portfolio sites | POI share in top-ranked cells | PC1 variance explained |
|---|---:|---:|---:|---:|---:|
| Berlin | 12,574 | 30,661 | 5 | 83.6% | 81.4% |
| Frankfurt | 4,119 | 8,476 | 5 | 81.7% | 75.4% |
| Muenchen | 4,540 | 13,740 | 5 | 68.3% | 79.8% |

**Interpretation:** The POI concentration statistic is an internal plausibility check, not an out-of-sample forecast of store revenue. The reference value stored in each plausibility JSON is 20%; definitions and sampling choices require inspection before making external predictive claims.

## Regression comparison (stored model report)

| Model | Stored out-of-sample explained deviance |
|---|---:|
| poisson | 47.43% |
| negativ_binomial | 51.30% |
| nb_raeumlich | 51.20% |

The stored report selects `negativ_binomial`. Its own methodological note states: Ohne S_c sind die Standardfehler zu klein, weil Nachbarzellen nicht unabhängig sind. lambda wurde auf derselben Kreuzvalidierung gewählt; der Vergleich ist für M3 leicht optimistisch.

## Reproduction status

- PASS: static Python compilation and structural consistency of versioned input/output tables (see `tests/`).
- NOT VERIFIED: regeneration of original census/OSM extracts from third-party endpoints.
- NOT VERIFIED: exact recomputation of all scores and regression estimates from a clean environment.
- NOT VERIFIED: predictive validity for new stores, turnover or investment returns.
- Streamlit cloud deployment has been reported working by the maintainer; this package does not independently test the remote service.

## Source attribution

See [`data/README.md`](data/README.md) for the Zensus 2022 and OpenStreetMap licenses and redistribution considerations.
