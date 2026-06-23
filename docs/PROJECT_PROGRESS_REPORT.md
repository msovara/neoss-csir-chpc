# NEOSS Climate Risk — Project Progress Report

**Repository:** [github.com/msovara/neoss-csir-chpc](https://github.com/msovara/neoss-csir-chpc)  
**Live app:** [neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app](https://neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app)  
**Report date:** June 2026 (updated)

---

## 1. Project purpose

The NEOSS–CSIR–CHPC collaboration is developing an **AI-powered environmental and climate risk mapping tool** for southern Africa. The focus is sub-seasonal to seasonal (S2S) hazards — heatwaves, wetland degradation, and wildfire — integrating Earth observation data, numerical weather modelling (WRF), and machine learning.

The Streamlit app is the **public-facing distribution platform**: a browser-based viewer for pre-computed risk maps from the October 2019 Limpopo heatwave and forest fire case study, plus operational S2S forecast products as they become available.

---

## 2. What we built

### 2.1 Repository and documentation

- Populated the GitHub repo with a project README (objectives and deliverables).
- Added `requirements.txt` (`streamlit>=1.28.0`) and `.streamlit/config.toml` (dark theme).
- Added `STREAMLIT_APP_METHODS_REPORT.md` (architecture and image-handling methods).
- Added this progress report (`PROJECT_PROGRESS_REPORT.md`).

### 2.2 Streamlit web application (`app.py`)

The app evolved through three stages:

| Stage | What was added |
|-------|----------------|
| **v1** | Single-purpose **Nylsvley Wetland Degradation Index (WDI)** viewer — 16 daily maps (15–30 Oct 2019) |
| **v2** | Added **Exceedance Maps** and **Fire Weather Index (FWI)** tabs |
| **v3 (current)** | Full **Hazard Risk Mapping Tool** with four main tabs |

**Current tab structure:**

1. **Case Study — Oct 2019** — Fire Risk, Wetland (EO–AI), Wetland WDI (NWP), Heatwave Risk (EO–AI CNN), Fire Weather Index
2. **S2S Heatwave Forecast** — weekly initialisation dates (rolling 12-week window)
3. **S2S Wetland Forecast** — same date logic
4. **S2S Wildfire Forecast** — initialisation date + forecast lead (week 1/2, month 1/2/3)

Each view includes a date selector, map display, info card, colour legend, and metadata in the sidebar.

### 2.3 Image assets

Risk maps are organised under a consistent folder structure:

```
images/case_study/fire/       fire_risk_YYYY-MM-DDT12.png
images/case_study/wetland/    wetland_risk_map_NN_YYYY-MM-DD.png
images/case_study/heatwave/   heatwave_risk_CNN_YYYY-MM-DD.png (preferred); heatwave_risk_YYYY-MM-DDT12.png (legacy)
images/forecasts/heatwave/    s2s_heatwave_YYYY-MM-DD.png
images/forecasts/wetland/     s2s_wetland_YYYY-MM-DD.png
images/forecasts/wildfire/    s2s_wildfire_YYYY-MM-DD_{lead}.png
```

**Case study inventory:**

| Layer | Maps loaded | Date coverage |
|-------|-------------|---------------|
| Fire | 11 | 20–30 Oct 2019 |
| Wetland | 15 | 15–29 Oct 2019 |
| Heatwave | 16 | 15–30 Oct 2019 (EO–AI CNN); legacy T12 maps retained where present |
| S2S heatwave / wetland | 0 | Folders ready — awaiting PNGs |
| S2S wildfire | 5 | Initialisation 15 May 2026 — see Section 4 |

### 2.4 Branding and UI design

- **Dark theme** — deep-space palette (`#0d1117` background, teal `#56cfe1` accents).
- **Typography** — Syne (headings) and Inter (body); badge, title, and subtitle sizes tuned iteratively.
- **Partner logos** stacked vertically in the header (CSIR, NICIS/CHPC, Limpopo Provincial Government / LEDET).
- **Header layout** — logos in a wider left column (`[3, 2]`), each at 420px width; title at 5rem so logos dominate visually.
- **Sidebar** — case study period, S2S forecast window, and data sources (WRF, ERA5, JRA-3Q, ECMWF S2S, EO).

### 2.5 Deployment

- Code pushed to GitHub (`main` branch).
- App deployed on **Streamlit Community Cloud**.
- Live URL: [neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app](https://neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app)

---

## 3. Technical approach

- **Static image viewer** — no server-side computation; all maps are pre-generated PNGs.
- **Path resolution** — helper functions match dates (and forecast leads) to filenames; missing files trigger user-facing warnings.
- **S2S date logic** — rolling 12-week window of Monday initialisation dates for heatwave/wetland tabs; wildfire tab auto-discovers available initialisation dates from the filesystem.
- **Responsive layout** — wide Streamlit layout, 3:1 map-to-info column split, images capped at 900px width.

---

## 4. S2S wildfire forecast figures (May 2026)

Five **Fire Occurrence Probability** maps were produced from a 3-member ECMWF S2S ensemble, initialised **15 May 2026**, covering the Limpopo region and surrounds (approx. 21–27°S, 25–33°E). All maps use the threshold **risk > 40%** for area statistics.

For this initialisation, the entire domain falls in the **0–5% (No Risk)** category — consistent with the dry-season transition period before peak fire weather. Area statistics report **0.0%** of the domain at P ≥ 60% and P ≥ 80%.

### 4.1 Sub-weekly leads

**Week 1 (Days 1–7): 15 May → 21 May 2026**

![Fire Occurrence Probability — Week 1](images/forecasts/wildfire/s2s_wildfire_2026-05-15_week1.png)

**Week 2 (Days 8–14): 22 May → 28 May 2026**

![Fire Occurrence Probability — Week 2](images/forecasts/wildfire/s2s_wildfire_2026-05-15_week2.png)

### 4.2 Monthly leads

**Month 1 (Days 1–30): 15 May → 13 June 2026**

![Fire Occurrence Probability — Month 1](images/forecasts/wildfire/s2s_wildfire_2026-05-15_month1.png)

**Month 2 (Days 31–60): 14 June → 13 July 2026**

![Fire Occurrence Probability — Month 2](images/forecasts/wildfire/s2s_wildfire_2026-05-15_month2.png)

**Month 3 (Days 61–90): 14 July → 12 August 2026**

![Fire Occurrence Probability — Month 3](images/forecasts/wildfire/s2s_wildfire_2026-05-15_month3.png)

### 4.3 Legend (all five figures)

| Probability | Category | Colour |
|-------------|----------|--------|
| 0–5% | No risk | White |
| 5–25% | Low | Light green |
| 25–40% | Moderate | Yellow |
| 40–70% | High | Orange |
| 70–100% | Very high | Red |

These figures are integrated into the **S2S Wildfire Forecast** tab of the Streamlit app. Select initialisation date **15 May 2026** and choose the desired forecast lead.

---

## 5. Git history (highlights)

- Redesign with case study + S2S forecast tabs
- CSIR, NICIS/CHPC, and Limpopo logos added and stacked vertically
- Header typography iterations (badge, title, subtitle sizing)
- Image max-width constraint (900px)
- Methods report added

---

## 6. Outstanding items

| Item | Status |
|------|--------|
| Push latest app changes (logos + wildfire figures) | Pending commit & push |
| Heatwave case-study gaps (22, 24–30 Oct) | 8 of 16 dates available |
| S2S heatwave / wetland forecast PNGs | Folders ready — awaiting operational outputs |
| Additional S2S wildfire initialisation dates | Only 15 May 2026 loaded so far |
| Update `STREAMLIT_APP_METHODS_REPORT.md` | Still describes old 3-tab layout |
| Local Python environment on Windows | Not configured — Cloud deployment is primary run path |

---

## 7. Summary

We progressed from an empty GitHub repo to a **deployed, branded Streamlit dashboard** that visualises the October 2019 Limpopo heatwave and fire case study across three hazard layers, with an operational framework for S2S forecast products. The first S2S wildfire outputs — five fire occurrence probability maps for May–August 2026 — are now in the repository, documented here, and viewable in the app under the **S2S Wildfire Forecast** tab.
