# Streamlit App — Methods Report

**Risk Mapping Tool for Climate and Environmental Risks**

---

## 1. Overview

This report describes the methods, architecture, and implementation approach used in the Streamlit web application for visualizing climate and environmental risk data. The app serves as an interactive dashboard for the October 2019 heatwave and forest fire case study.

---

## 2. Application Architecture

### 2.1 Technology Stack

| Component | Technology |
|-----------|------------|
| Framework | Streamlit 1.28+ |
| Language | Python 3 |
| File handling | `pathlib.Path` |
| Date formatting | `datetime` |

### 2.2 Layout Structure

- **Page configuration**: Wide layout (`layout="wide"`), expanded sidebar
- **Theme**: Dark theme (`#1a1a2e` background, `#16213e` secondary)
- **Navigation**: Tab-based interface with three main sections

---

## 3. Core Methods

### 3.1 Image Path Resolution

Three helper functions resolve file paths for different types of imagery:

| Method | Purpose | Naming Convention |
|--------|---------|-------------------|
| `get_image_path(date_str)` | Resolves WDI (Wetland Degradation Index) images | `Nylsvley_WDIwrf_YYYY-MM-DD.png` |
| `get_exceedance_path(date_str)` | Resolves exceedance map images | `exceedance_YYYY-MM-DD.png` |
| `get_fwi_path(date_str)` | Resolves Fire Weather Index images | `FWI_baseline_YYYY-MM-DD.png` |

**Implementation approach**:
- Uses `Path(__file__).parent / "images"` for a portable base directory
- Checks for exact filename match first
- `get_image_path` includes a fallback glob search for files containing the date
- Returns `None` if file does not exist

### 3.2 Data Display

- **Static images**: Pre-generated PNG maps stored in `images/` directory
- **No server-side computation**: All visualizations are pre-computed; the app serves images only
- **Date selection**: User selects date via `st.selectbox`; app loads the corresponding image

---

## 4. User Interface Methods

### 4.1 Tab Organization

| Tab | Content | Date Range |
|-----|---------|------------|
| Nylsvley WDI | Wetland Degradation Index for Nylsvley region | 15–30 Oct 2019 (16 dates) |
| Exceedance Maps | Regional exceedance events (red dots) | 15–23 Oct 2019 (8–9 dates) |
| Fire Weather Index | FWI baseline maps for Southern Africa | 15–30 Oct 2019 (16 dates) |

### 4.2 Interaction Flow

1. User selects a tab
2. User selects a date from the dropdown
3. App resolves the image path and displays it via `st.image()`
4. Optional expanders provide context and methodology descriptions

### 4.3 Styling

- **Custom CSS**: Injected via `st.markdown(..., unsafe_allow_html=True)`
- **Header**: 10rem font size, light colour on dark background
- **Images**: Max-width 900px, rounded corners, shadow
- **Theme**: Dark theme via `.streamlit/config.toml`

---

## 5. Deployment Method

### 5.1 Local Execution

```bash
streamlit run app.py
```

### 5.2 Hosting

- **Platform**: Streamlit Community Cloud (share.streamlit.io)
- **Source**: GitHub repository (`msovara/neoss-csir-chpc`)
- **Entry point**: `app.py`
- **Dependencies**: `requirements.txt` (Streamlit only)

---

## 6. Data Sources and Visualizations

| Dataset | Description | Spatial Extent |
|---------|-------------|-----------------|
| WDI | Wetland Degradation Index (WRF model output) | Nylsvley region (~28.65–28.75°E, ~24.58–24.72°S) |
| Exceedance | Threshold exceedance events | Southern Africa (~25–33°E, ~21–27°S) |
| FWI | Fire Weather Index (baseline) | Southern Africa (~26–33°E, ~22–27°S) |

---

## 7. Limitations and Future Enhancements

- **Static images**: No live computation or dynamic plotting
- **Fixed date range**: No user-defined date range
- **No data export**: No download or export of underlying data
- **Potential future**: Interactive maps (e.g. Folium/Plotly), real-time data, and user-defined date ranges

---

## 8. File Structure

```
neoss-csir-chpc/
├── app.py                 # Main app entry point
├── requirements.txt       # Dependencies
├── .streamlit/
│   └── config.toml       # Theme and server config
├── images/               # Pre-generated imagery
│   ├── Nylsvley_WDIwrf_*.png
│   ├── exceedance_*.png
│   └── FWI_baseline_*.png
└── README.md
```

---

*Report generated for the NEOSS Climate Risk project.*
