# Geospatial Market Potential & Site Selection Analytics

**Oliver Wyman × STADS Data & Analytics Hackathon 2026 | Team Project**

*An interactive, data-driven framework for evaluating retail location attractiveness, competitive intensity, and geographic market opportunities.*

## Project Overview

This project explores how geospatial data, statistical modelling, and interactive analytics can support retail site selection and market expansion decisions.

Developed during the Oliver Wyman × STADS Data & Analytics Hackathon 2026, the solution examines potential market opportunities for premium grocery retail across **Berlin, Frankfurt, and Munich**.

The objective is to translate heterogeneous geographic and demographic information into an interpretable decision-support framework, rather than relying solely on descriptive maps or individual location indicators.

## Analytical Framework

The project combines several analytical components:

- **Geospatial data processing:** Integration and preparation of demographic and geographic information, including census-based and OpenStreetMap-derived inputs.
- **Spatial aggregation:** Geographic analysis using H3 hexagonal grids.
- **Market attractiveness:** Evaluation of local demand-related indicators and accessibility.
- **Competitive intensity:** Distance-sensitive modelling of nearby retail alternatives, including a Huff-inspired approach.
- **Statistical modelling:** Application of dimensionality reduction and regression-based methods within the analytical workflow.
- **Scenario exploration:** Interactive comparison of assumptions and location-related indicators.

The resulting application is designed to help users explore geographic patterns, compare locations, and understand how modelling assumptions influence analytical outputs.

## Geographic Scope

- Berlin, Germany
- Frankfurt am Main, Germany
- Munich, Germany

## Technology Stack

**Python · pandas · NumPy · Geospatial Analytics · H3 · scikit-learn · Streamlit**

*The exact dependencies are documented in `requirements.txt`.*

## Repository Structure

The application currently includes modules for data preparation, analytical modelling, methodology, concept development, location comparison, and an interactive Streamlit interface.

A detailed module-level overview and reproducible setup instructions will be added after the code and data dependencies have been verified.

## Interactive Dashboard

The Streamlit application provides a visual interface for exploring the geographic analysis and comparing location-related indicators.

*Dashboard screenshots and a short demonstration video will be added to this section.*

## Methodological Considerations

The analysis is an exploratory hackathon prototype. Its outputs depend on the available data, geographic aggregation choices, model specifications, and selected parameters.

The results should be interpreted as analytical decision support rather than validated commercial forecasts or definitive investment recommendations.

## Project Context & Credits

Developed collaboratively during the **Oliver Wyman × STADS Data & Analytics Hackathon 2026**.

This repository is a portfolio-oriented presentation of the team project, retaining attribution to the original collaborative development.

**Original team repository:** [annaantoniya/ow_hackathon_group1](https://github.com/annaantoniya/ow_hackathon_group1)

**Portfolio maintained by:** Katharina Luran Chen

*Individual contributions and additional technical documentation will be specified in subsequent updates.*
