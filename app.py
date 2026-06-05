"""
NEOSS Climate Risk — Interactive Risk Mapping Tool
===================================================
Tabs:
  1. Case Study (Oct 2019 heatwave & wildfire event)
       - Fire Risk
       - Wetland Risk (EO–AI hybrid)
       - Wetland WDI (NWP)
       - Heatwave Risk
       - Fire Weather Index (NWP matrix)
  2. S2S Heatwave Forecast     (date-driven, real-time)
  3. S2S Wetland Forecast      (date-driven, real-time)
  4. S2S Wildfire Risk Forecast (date-driven, real-time)

GitHub: https://github.com/msovara/neoss-csir-chpc
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import streamlit as st

# ──────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Hazard Risk Mapping Tool",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS  (deep-space dark theme with teal/amber accents)
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
/* ── Global background ──────────────────────────── */
.stApp,
.main,
[data-testid="stAppViewContainer"] {
    background-color: #0d1117;
}
.stApp > header { background-color: #0d1117; }

/* ── Sidebar ────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: #161b22;
    border-right: 1px solid #21262d;
}
[data-testid="stSidebar"] * { color: #c9d1d9 !important; }

/* ── Typography ─────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@300;400;500&display=swap');

.neoss-title {
    font-family: 'Syne', sans-serif;
    font-size: 5rem;
    font-weight: 800;
    color: #e6edf3;
    letter-spacing: -0.02em;
    line-height: 1.05;
    margin-bottom: 0.5rem;
}
.neoss-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 2.2rem;
    font-weight: 400;
    color: #8b949e;
    margin-bottom: 1rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.neoss-badge {
    display: inline-block;
    background: linear-gradient(135deg, #1a3a4a 0%, #0e2d3a 100%);
    border: 1px solid #2d6a7f;
    color: #56cfe1;
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.3rem 1rem;
    border-radius: 100px;
    margin-right: 0.5rem;
    margin-bottom: 0.6rem;
}
.logo-wrap {
    background: #ffffff;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    display: inline-block;
    margin-bottom: 1rem;
    border: 1px solid #21262d;
}
.logo-wrap img {
    max-height: 56px;
    width: auto;
    display: block;
}

/* ── Tabs ───────────────────────────────────────── */
[data-testid="stTabs"] [role="tablist"] {
    gap: 0.25rem;
    border-bottom: 1px solid #21262d;
    padding-bottom: 0;
}
[data-testid="stTabs"] [role="tab"] {
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #8b949e;
    border-radius: 6px 6px 0 0;
    padding: 0.55rem 1.2rem;
    border: 1px solid transparent;
    border-bottom: none;
    transition: color 0.2s, background 0.2s;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: #56cfe1 !important;
    background: #161b22;
    border-color: #21262d;
    border-bottom-color: #161b22;
}
[data-testid="stTabs"] [role="tab"]:hover { color: #c9d1d9 !important; }

/* ── Cards / containers ─────────────────────────── */
.risk-card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
}
.risk-card h4 {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #e6edf3;
    margin: 0 0 0.25rem 0;
}
.risk-card p {
    font-family: 'Inter', sans-serif;
    font-size: 0.82rem;
    color: #8b949e;
    margin: 0;
    line-height: 1.5;
}

/* ── Legend chips ───────────────────────────────── */
.legend-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.5rem; }
.legend-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    color: #c9d1d9;
    background: #21262d;
    border-radius: 100px;
    padding: 0.18rem 0.65rem;
}
.chip-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}

/* ── Date selector label ────────────────────────── */
.date-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #8b949e;
    margin-bottom: 0.25rem;
}

/* ── Image frame ────────────────────────────────── */
.stImage img {
    border-radius: 8px;
    border: 1px solid #21262d;
    box-shadow: 0 4px 24px rgba(0,0,0,0.6);
    max-width: 900px !important;
    width: auto !important;
    height: auto !important;
}

/* ── Warning / info ─────────────────────────────── */
[data-testid="stAlert"] {
    background: #1c2128;
    border: 1px solid #30363d;
    border-radius: 8px;
}

/* ── Selectbox ──────────────────────────────────── */
[data-testid="stSelectbox"] > div > div {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    color: #c9d1d9;
}

/* ── Sub-section header ─────────────────────────── */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #e6edf3;
    margin: 0.5rem 0 0.1rem 0;
}
.section-meta {
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem;
    color: #8b949e;
    margin-bottom: 1rem;
}

/* ── Radio buttons (sub-tab selector) ──────────── */
[data-testid="stRadio"] label {
    font-family: 'Inter', sans-serif;
    font-size: 0.82rem;
    color: #c9d1d9;
}
[data-testid="stRadio"] { margin-bottom: 0.8rem; }

/* ── Divider ────────────────────────────────────── */
hr { border-color: #21262d; }
</style>
""",
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────────
# PATHS
# ──────────────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "assets" / "csir_logo.png"
NICIS_CHPC_LOGO_PATH = BASE_DIR / "assets" / "nicis_chpc_logo.png"
LIMPOPO_LOGO_PATH = BASE_DIR / "assets" / "limpopo_ledet_logo.png"

FIRE_DIR = BASE_DIR / "images" / "case_study" / "fire"
WETLAND_DIR = BASE_DIR / "images" / "case_study" / "wetland"
WETLAND_NWP_DIR = BASE_DIR / "images" / "case_study" / "wetland_nwp"
HEATWAVE_DIR = BASE_DIR / "images" / "case_study" / "heatwave"
FWI_DIR = BASE_DIR / "images" / "case_study" / "fwi"
FWI_MATRIX_PATH = FWI_DIR / "fwi_nwp_matrix.png"

S2S_HW_DIR = BASE_DIR / "images" / "forecasts" / "heatwave"
S2S_WL_DIR = BASE_DIR / "images" / "forecasts" / "wetland"
S2S_WF_DIR = BASE_DIR / "images" / "forecasts" / "wildfire"

DATE_FMT = "%Y-%m-%d"


def fmt_date(d: str) -> str:
    return datetime.strptime(d, DATE_FMT).strftime("%d %B %Y")


def _weekly_dates(start: str, n_weeks: int) -> list[str]:
    base = datetime.strptime(start, DATE_FMT)
    return [(base + timedelta(weeks=i)).strftime(DATE_FMT) for i in range(n_weeks)]


def fire_path(date_str: str) -> Path | None:
    p = FIRE_DIR / f"fire_risk_{date_str}T12.png"
    return p if p.exists() else None


def wetland_path(date_str: str) -> Path | None:
    matches = sorted(WETLAND_DIR.glob(f"wetland_risk_map_*_{date_str}.png"))
    return matches[0] if matches else None


def wetland_nwp_path(date_str: str) -> Path | None:
    p = WETLAND_NWP_DIR / f"wdi_wetland_nwp_{date_str}.png"
    return p if p.exists() else None


def heatwave_path(date_str: str) -> Path | None:
    p = HEATWAVE_DIR / f"heatwave_risk_{date_str}T12.png"
    return p if p.exists() else None


CASE_STUDY_CANDIDATES = [f"2019-10-{d:02d}" for d in range(15, 31)]

FIRE_DATES = [d for d in CASE_STUDY_CANDIDATES if fire_path(d)]
WETLAND_DATES = [d for d in CASE_STUDY_CANDIDATES if wetland_path(d)]
WETLAND_NWP_DATES = [d for d in CASE_STUDY_CANDIDATES if wetland_nwp_path(d)]
HEATWAVE_DATES = [d for d in CASE_STUDY_CANDIDATES if heatwave_path(d)]


_TODAY = datetime.utcnow()
_LATEST_MON = _TODAY - timedelta(days=_TODAY.weekday())
_S2S_START = (_LATEST_MON - timedelta(weeks=11)).strftime(DATE_FMT)
S2S_DATES = _weekly_dates(_S2S_START, n_weeks=12)


def s2s_hw_path(date_str: str) -> Path | None:
    p = S2S_HW_DIR / f"s2s_heatwave_{date_str}.png"
    return p if p.exists() else None


def s2s_wl_path(date_str: str) -> Path | None:
    p = S2S_WL_DIR / f"s2s_wetland_{date_str}.png"
    return p if p.exists() else None


def s2s_wf_path(date_str: str, lead: str = "week1") -> Path | None:
    p = S2S_WF_DIR / f"s2s_wildfire_{date_str}_{lead}.png"
    if p.exists():
        return p
    p_legacy = S2S_WF_DIR / f"s2s_wildfire_{date_str}.png"
    return p_legacy if p_legacy.exists() else None


S2S_WF_LEADS: dict[str, str] = {
    "Week 1 (Days 1–7)": "week1",
    "Week 2 (Days 8–14)": "week2",
    "Month 1 (Days 1–30)": "month1",
    "Month 2 (Days 31–60)": "month2",
    "Month 3 (Days 61–90)": "month3",
}


def _discover_s2s_inits(directory: Path, prefix: str) -> list[str]:
    inits: set[str] = set()
    for f in directory.glob(f"{prefix}_*.png"):
        rest = f.stem[len(prefix) + 1 :]
        date_part = rest.split("_")[0]
        if len(date_part) == 10 and date_part[4] == "-" and date_part[7] == "-":
            inits.add(date_part)
    return sorted(inits, reverse=True)


S2S_HW_INIT_DATES = _discover_s2s_inits(S2S_HW_DIR, "s2s_heatwave")
S2S_WL_INIT_DATES = _discover_s2s_inits(S2S_WL_DIR, "s2s_wetland")
S2S_WF_INIT_DATES = _discover_s2s_inits(S2S_WF_DIR, "s2s_wildfire")


def show_image_or_warning(path: Path | None, label: str):
    if path and path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.warning(
            f"Image not found for **{label}**. "
            "Ensure the correct `images/` sub-folder is populated.",
            icon=None,
        )


def show_s2s_forecast(
    *,
    key_prefix: str,
    init_dates: list[str],
    path_fn,
    folder: str,
    filename_pattern: str,
):
    if not init_dates:
        st.info(
            f"No S2S forecast images are loaded yet. Add PNG files to "
            f"`{folder}` named `{filename_pattern}`. "
            "Only dates with available maps appear in the selector."
        )
        return
    selected = date_selector(
        f"{key_prefix}_date",
        init_dates,
        label="Initialisation date",
    )
    show_image_or_warning(path_fn(selected), selected)


def date_selector(key: str, dates: list[str], label: str = "Select date") -> str:
    st.markdown(f'<p class="date-label">{label}</p>', unsafe_allow_html=True)
    return st.selectbox(
        label,
        options=dates,
        format_func=fmt_date,
        key=key,
        label_visibility="collapsed",
    )


def info_card(title: str, body: str):
    st.markdown(
        f'<div class="risk-card"><h4>{title}</h4><p>{body}</p></div>',
        unsafe_allow_html=True,
    )


def legend_chips(chips: list[tuple[str, str]]):
    dots = "".join(
        f'<span class="legend-chip">'
        f'<span class="chip-dot" style="background:{col}"></span>{lbl}'
        f"</span>"
        for col, lbl in chips
    )
    st.markdown(f'<div class="legend-row">{dots}</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────────────────────────────────────
header_logos, header_text = st.columns([2, 3], gap="medium")

with header_logos:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=240)
    else:
        st.caption("CSIR logo not found")
    if NICIS_CHPC_LOGO_PATH.exists():
        st.image(str(NICIS_CHPC_LOGO_PATH), width=240)
    else:
        st.caption("NICIS/CHPC logo not found")
    if LIMPOPO_LOGO_PATH.exists():
        st.image(str(LIMPOPO_LOGO_PATH), width=240)
    else:
        st.caption("Limpopo logo not found")

with header_text:
    st.markdown(
        """
        <span class="neoss-badge">NEOSS · CSIR · CHPC</span>
        <span class="neoss-badge">Southern Africa</span>
        <span class="neoss-badge">NWP-EO_AI modelling</span>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<p class="neoss-title">🌍 Hazard Risk Mapping Tool</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="neoss-subtitle">Environmental & climate risk intelligence for southern Africa</p>',
        unsafe_allow_html=True,
    )

st.markdown("---")

tab_cs, tab_hw, tab_wl, tab_wf = st.tabs([
    " Case Study — Oct 2019",
    " S2S Heatwave Forecast",
    " S2S Wetland Forecast",
    " S2S Wildfire Forecast",
])

with tab_cs:
    st.markdown(
        '<p class="section-header">October 2019 Heatwave &amp; Forest Fire Event</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="section-meta">Nylsvley &amp; Southern Africa region · WRF model output · Select a risk layer and date below</p>',
        unsafe_allow_html=True,
    )

    layer = st.radio(
        "Risk layer",
        options=[
            "Fire Risk",
            "Wetland Risk (EO–AI hybrid)",
            "Wetland WDI (NWP)",
            "Heatwave Risk",
            "Fire Weather Index (NWP)",
        ],
        horizontal=True,
        key="cs_layer",
    )

    st.markdown("")
    col_map, col_info = st.columns([3, 1], gap="medium")

    if "Fire Risk" in layer:
        with col_map:
            if FIRE_DATES:
                selected = date_selector("fire_date", FIRE_DATES)
                show_image_or_warning(fire_path(selected), selected)
            else:
                st.info("No fire risk maps found in `images/case_study/fire/`.")
        with col_info:
            info_card(
                "Fire Risk",
                "Daily fire risk severity for the southern Africa region, "
                "derived from WRF atmospheric model output for the October 2019 "
                "heatwave and forest fire event.",
            )
            legend_chips([
                ("#fff5e0", "Low"),
                ("#ffa94d", "Moderate"),
                ("#e03131", "High"),
                ("#2d0a0a", "Extreme"),
            ])
            st.markdown("")
            st.caption("Files: `fire_risk_YYYY-MM-DDT12.png`")
            st.caption("Period: 15 – 30 October 2019  ·  12:00 UTC")

    elif layer.startswith("Wetland Risk"):
        with col_map:
            if WETLAND_DATES:
                selected = date_selector("wetland_date", WETLAND_DATES)
                show_image_or_warning(wetland_path(selected), selected)
            else:
                st.info("No hybrid wetland maps found in `images/case_study/wetland/`.")
        with col_info:
            info_card(
                "Wetland Risk (EO–AI hybrid)",
                "EO- and AI-enhanced wetland degradation risk maps for selected "
                "Limpopo wetlands (Baleni, Khurini, Nylsvley, Makuleke, Sekhukhune). "
                "Combines WRF-based WDI with CNN residual correction from MODIS "
                "and Sentinel-2 indicators.",
            )
            legend_chips([
                ("#1c6ef5", "Water surplus"),
                ("#adb5bd", "Near normal"),
                ("#c0392b", "Water deficit"),
            ])
            st.markdown("")
            st.caption("Files: `wetland_risk_map_NN_YYYY-MM-DD.png`")
            st.caption("Period: 15 – 30 October 2019")

    elif layer.startswith("Wetland WDI"):
        with col_map:
            if WETLAND_NWP_DATES:
                selected = date_selector("wetland_nwp_date", WETLAND_NWP_DATES)
                show_image_or_warning(wetland_nwp_path(selected), selected)
            else:
                st.info("No NWP WDI maps found in `images/case_study/wetland_nwp/`.")
        with col_info:
            info_card(
                "Wetland WDI (NWP)",
                "WRF-based Wetland Degradation Index (WDI) from model output "
                "variables: climatic water balance, soil moisture, temperature, "
                "wind, and relative humidity (He et al., 2022 formulation).",
            )
            legend_chips([
                ("#1c6ef5", "Surplus  (WDI > 0)"),
                ("#adb5bd", "Near normal"),
                ("#c0392b", "Deficit  (WDI < 0)"),
            ])
            st.markdown("")
            st.caption("Files: `wdi_wetland_nwp_YYYY-MM-DD.png`")
            st.caption("Period: 15 – 30 October 2019")

    elif "Fire Weather" in layer:
        with col_map:
            if FWI_MATRIX_PATH.exists():
                st.image(str(FWI_MATRIX_PATH), use_container_width=True)
            else:
                st.info("No FWI matrix found in `images/case_study/fwi/`.")
        with col_info:
            info_card(
                "Fire Weather Index (NWP)",
                "Canadian FWI components (FFMC, DMC, DC, ISI, BUI, FWI) derived "
                "from WRF surface meteorology at daily noon for the case-study "
                "period, shown as a multi-panel summary matrix.",
            )
            legend_chips([
                ("#fff5e0", "Low"),
                ("#ffa94d", "Moderate"),
                ("#e03131", "High"),
                ("#2d0a0a", "Extreme"),
            ])
            st.markdown("")
            st.caption("File: `fwi_nwp_matrix.png`")
            st.caption("Period: 15 – 30 October 2019  ·  NWP baseline")

    else:
        with col_map:
            if HEATWAVE_DATES:
                selected = date_selector("hw_date", HEATWAVE_DATES)
                show_image_or_warning(heatwave_path(selected), selected)
            else:
                st.info("No heatwave maps found in `images/case_study/heatwave/`.")
        with col_info:
            info_card(
                "Heatwave Risk",
                "Daily heatwave risk intensity maps showing temperature anomaly "
                "and exceedance thresholds during the "
                "October 2019 extreme heat event.",
            )
            legend_chips([
                ("#74c0fc", "Below avg"),
                ("#ffd43b", "Elevated"),
                ("#f76707", "Heatwave"),
                ("#9c36b5", "Extreme"),
            ])
            st.markdown("")
            st.caption("Files: `heatwave_risk_YYYY-MM-DDT12.png`")
            st.caption("Period: 15 – 30 October 2019  ·  12:00 UTC")

with tab_hw:
    st.markdown(
        '<p class="section-header">Real-Time S2S Heatwave Forecast</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="section-meta">'
        "Sub-seasonal to seasonal heatwave risk projections · Updated operationally · "
        "Select an initialisation date below"
        "</p>",
        unsafe_allow_html=True,
    )
    col_map2, col_info2 = st.columns([3, 1], gap="medium")
    with col_map2:
        show_s2s_forecast(
            key_prefix="s2s_hw",
            init_dates=S2S_HW_INIT_DATES,
            path_fn=s2s_hw_path,
            folder="images/forecasts/heatwave/",
            filename_pattern="s2s_heatwave_YYYY-MM-DD.png",
        )
    with col_info2:
        info_card(
            "S2S Heatwave Forecast",
            "Sub-seasonal to seasonal probabilistic heatwave forecast. "
            "Shows temperature exceedance probabilities at 2-week to "
            "2-month lead times, derived from ECMWF S2S ensemble output.",
        )
        legend_chips([
            ("#74c0fc", "< 25 %"),
            ("#ffd43b", "25 – 50 %"),
            ("#f76707", "50 – 75 %"),
            ("#e03131", "> 75 %"),
        ])
        st.markdown("")
        st.caption("Files: `s2s_heatwave_YYYY-MM-DD.png`")
        st.caption("Frequency: weekly initialisation  ·  Lead: 2 wk – 2 mo")
        st.caption("Source: ECMWF S2S database · ERA5 climatology")

with tab_wl:
    st.markdown(
        '<p class="section-header">Real-Time S2S Wetland Degradation Forecast</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="section-meta">'
        "Sub-seasonal to seasonal wetland stress projections · Updated operationally · "
        "Select an initialisation date below"
        "</p>",
        unsafe_allow_html=True,
    )
    col_map3, col_info3 = st.columns([3, 1], gap="medium")
    with col_map3:
        show_s2s_forecast(
            key_prefix="s2s_wl",
            init_dates=S2S_WL_INIT_DATES,
            path_fn=s2s_wl_path,
            folder="images/forecasts/wetland/",
            filename_pattern="s2s_wetland_YYYY-MM-DD.png",
        )
    with col_info3:
        info_card(
            "S2S Wetland Forecast",
            "Probabilistic wetland degradation risk at S2S lead times. "
            "Combines soil-moisture ensemble spread with vegetation stress "
            "indicators. The Nylsvley Nature Reserve boundary is overlaid "
            "as reference.",
        )
        legend_chips([
            ("#1c6ef5", "Surplus  (WDI > 1)"),
            ("#adb5bd", "Near normal"),
            ("#e8a838", "Mild deficit"),
            ("#c0392b", "Severe deficit"),
        ])
        st.markdown("")
        st.caption("Files: `s2s_wetland_YYYY-MM-DD.png`")
        st.caption("Frequency: weekly initialisation  ·  Lead: 2 wk – 2 mo")
        st.caption("WDI range: −2.0 (severe deficit) to +2.0 (surplus)")

with tab_wf:
    st.markdown(
        '<p class="section-header">Real-Time S2S Wildfire Risk Forecast</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="section-meta">'
        "Sub-seasonal to seasonal fire occurrence probability · Updated operationally · "
        "Select initialisation date and forecast lead below"
        "</p>",
        unsafe_allow_html=True,
    )
    col_map4, col_info4 = st.columns([3, 1], gap="medium")
    with col_map4:
        if not S2S_WF_INIT_DATES:
            st.info(
                "No S2S wildfire forecast images are loaded yet. Add PNG files to "
                "`images/forecasts/wildfire/` named "
                "`s2s_wildfire_YYYY-MM-DD_{lead}.png` "
                "(leads: week1, week2, month1, month2, month3)."
            )
        else:
            selected_wf = date_selector(
                "s2s_wf_date",
                S2S_WF_INIT_DATES,
                label="Initialisation date",
            )
            lead_label = st.selectbox(
                "Forecast lead",
                options=list(S2S_WF_LEADS.keys()),
                key="s2s_wf_lead",
            )
            lead_key = S2S_WF_LEADS[lead_label]
            show_image_or_warning(
                s2s_wf_path(selected_wf, lead_key),
                f"{selected_wf} · {lead_label}",
            )
    with col_info4:
        info_card(
            "S2S Wildfire Risk Forecast",
            "Ensemble-based fire occurrence probability maps for the Limpopo "
            "region and surrounds. Shows P(fire on any day in period) at "
            "sub-weekly to seasonal lead times from ECMWF S2S output "
            "(3 ensemble members).",
        )
        legend_chips([
            ("#ffffff", "No risk  (0–5 %)"),
            ("#b2f2bb", "Low  (5–25 %)"),
            ("#ffd43b", "Moderate  (25–40 %)"),
            ("#f76707", "High  (40–70 %)"),
            ("#e03131", "Very high  (70–100 %)"),
        ])
        st.markdown("")
        st.caption("Files: `s2s_wildfire_YYYY-MM-DD_{lead}.png`")
        st.caption("Leads: week1, week2, month1, month2, month3")
        st.caption("Source: ECMWF S2S database · 3-member ensemble")

with st.sidebar:
    st.markdown("Environmental and Climate Risk Mapping")
    st.caption(
        "Interactive risk mapping tool for South Africa, "
        "developed as part of the NEOSS-CSIR-CHPC collaboration."
    )
    st.divider()
    st.markdown("**Case Study Period**")
    st.caption("15 – 30 October 2019\nHeatwave & forest fire event\nover Limpopo, South Africa")
    st.divider()
    st.markdown("**S2S Forecast Period**")
    st.caption(
        f"Weekly initialisations\n"
        f"{fmt_date(S2S_DATES[0])} → {fmt_date(S2S_DATES[-1])}\n"
        "Lead time: 2 weeks – 3 months"
    )
    st.divider()
    st.markdown("**Data Sources**")
    st.caption(
        "• WRF mesoscale model output\n"
        "• ERA5 reanalysis climatology\n"
        "• JRA-3Q reanalysis climatology\n"
        "• Historical Earth Observations\n"
        "• Near-real-time Earth Observations\n"
        "• ECMWF S2S database"
    )
    st.divider()
    st.markdown("[🔗 View on GitHub](https://github.com/msovara/neoss-csir-chpc)")
    st.caption("CSIR · CHPC · NEOSS")
