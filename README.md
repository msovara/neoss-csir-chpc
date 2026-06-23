# NEOSS Climate Risk — Hazard Risk Mapping Tool

[![GitHub](https://img.shields.io/badge/GitHub-neoss--csir--chpc-blue)](https://github.com/msovara/neoss-csir-chpc)
[![Streamlit App](https://img.shields.io/badge/Live%20app-Streamlit-FF4B4B)](https://neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app)

**NEOSS–CSIR–CHPC** collaboration · **LEDET** provincial partner · aligned with **WeEarth Farm Vision** GIS monitoring

---

## Live dashboard

**[Open the Hazard Risk Mapping Tool →](https://neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app)**

Browser-based viewer for pre-computed climate and environmental risk maps: October 2019 Limpopo case study plus sub-seasonal to seasonal (S2S) forecast prototypes.

---

## Project overview

This project develops an **AI-powered monitoring and risk-mapping tool** for severe weather and environmental hazards at **sub-seasonal to seasonal (S2S)** timescales (2 weeks to 3 months ahead). It integrates:

- **Numerical weather prediction (NWP)** — WRF simulations and derived indices (e.g. FWI, WDI)
- **Near-real-time Earth observation (EO)** — MODIS, VIIRS, Sentinel-derived products
- **Machine learning** — CNN / ConvLSTM hazard enhancement
- **High-performance computing** — CSIR Centre for High Performance Computing (CHPC) Lengau

The tool supports disaster risk preparedness, climate adaptation, and evidence-based policy — with emphasis on **heatwaves**, **wildfire**, and **wetland degradation** in southern Africa.

---

## Case study — October 2019 Limpopo

Heatwave and forest fire event (15–30 October 2019), including Thabazimbi and Nylsvley wetland impacts. The dashboard replays daily hazard layers showing event **onset, intensification, peak, and decay**.

| Layer | Method | Files |
|-------|--------|-------|
| Fire risk | EO–AI / WRF-based | `fire_risk_YYYY-MM-DDT12.png` |
| Fire weather (FWI) | NWP matrix | `fwi_nwp_matrix.png` |
| Wetland risk | EO–AI hybrid | `wetland_risk_map_NN_YYYY-MM-DD.png` |
| Wetland WDI | NWP | `wdi_wetland_nwp_YYYY-MM-DD.png` |
| Heatwave risk | EO–AI CNN | `heatwave_risk_CNN_YYYY-MM-DD.png` |

---

## App structure

| Tab | Content |
|-----|---------|
| **Case Study — Oct 2019** | Fire Risk · Wetland (EO–AI) · Wetland WDI (NWP) · Heatwave Risk · Fire Weather Index |
| **S2S Heatwave Forecast** | Weekly initialisation dates (rolling 12-week window) |
| **S2S Wetland Forecast** | Weekly initialisation dates |
| **S2S Wildfire Forecast** | Initialisation date + lead (week 1/2, month 1/2/3) |

---

## Repository layout

```
neoss-csir-chpc/
├── app.py                          # Streamlit application
├── requirements.txt
├── .streamlit/config.toml          # Dark theme
├── assets/                         # CSIR, CHPC, LEDET logos
├── images/
│   ├── case_study/
│   │   ├── fire/
│   │   ├── fwi/
│   │   ├── heatwave/               # heatwave_risk_CNN_YYYY-MM-DD.png
│   │   ├── wetland/
│   │   └── wetland_nwp/
│   └── forecasts/
│       ├── heatwave/               # s2s_heatwave_YYYY-MM-DD.png
│       ├── wetland/                # s2s_wetland_YYYY-MM-DD.png
│       └── wildfire/               # s2s_wildfire_YYYY-MM-DD_{lead}.png
└── docs/
    ├── PROJECT_PROGRESS_REPORT.md
    ├── STREAMLIT_APP_METHODS_REPORT.md
    ├── WEEARTH_SPACE_HUB_ALIGNMENT.md
    ├── WEEARTH_TIA_LEDET_MAPPING.md
    └── WEEARTH_PILOT_COMMUNITY_AND_SCALE.md
```

Add new map PNGs under the matching folder; the app discovers available dates automatically.

---

## Run locally

```bash
git clone https://github.com/msovara/neoss-csir-chpc.git
cd neoss-csir-chpc
pip install -r requirements.txt
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501).

---

## WeEarth / Farm Vision alignment

This tool is the **technical engine** for CSIR climate and environmental risk intelligence in the **TIA-supported WeEarth Farm Vision Commercialisation Programme**:

- GIS-ready hazard layers for Space Hub and Farm Vision workflows
- Municipal- and ward-scale products (Limpopo / LEDET pilot pathway)
- Disaster monitoring for agriculture, water, and livelihoods
- Documented 3-month pilot scope for national scale-up

See [`docs/WEEARTH_SPACE_HUB_ALIGNMENT.md`](docs/WEEARTH_SPACE_HUB_ALIGNMENT.md) and [`docs/WEEARTH_TIA_LEDET_MAPPING.md`](docs/WEEARTH_TIA_LEDET_MAPPING.md) for implementation mapping.

---

## Documentation

| Document | Description |
|----------|-------------|
| [docs/PROJECT_PROGRESS_REPORT.md](docs/PROJECT_PROGRESS_REPORT.md) | Build history, assets inventory, deployment |
| [docs/STREAMLIT_APP_METHODS_REPORT.md](docs/STREAMLIT_APP_METHODS_REPORT.md) | App architecture and image handling |
| [docs/WEEARTH_SPACE_HUB_ALIGNMENT.md](docs/WEEARTH_SPACE_HUB_ALIGNMENT.md) | Programme positioning (4-layer model) |
| [docs/WEEARTH_TIA_LEDET_MAPPING.md](docs/WEEARTH_TIA_LEDET_MAPPING.md) | WeEarth needs ↔ CSIR tool ↔ LEDET |
| [docs/WEEARTH_PILOT_COMMUNITY_AND_SCALE.md](docs/WEEARTH_PILOT_COMMUNITY_AND_SCALE.md) | Community engagement, scale-up, 3-month pilot |

---

## Partners

- **CSIR** — climate and environmental risk science
- **CHPC (NICIS)** — high-performance computing infrastructure
- **LEDET** — Limpopo Provincial Government
- **NEOSS** — programme umbrella
- **WeEarth Farm Vision** — commercialisation and GIS practitioner deployment

---

## Licence and citation

Developed under the NEOSS programme. If you use this tool or maps in reports, please cite the NEOSS–CSIR–CHPC Hazard Risk Mapping Tool and acknowledge CSIR, CHPC, and LEDET.

**Repository:** [github.com/msovara/neoss-csir-chpc](https://github.com/msovara/neoss-csir-chpc)
