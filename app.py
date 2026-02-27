"""
NEOSS Climate Risk - Nylsvley WDI Visualization

Interactive Streamlit app for visualizing the Wetland Degradation Index (WDI)
for the Nylsvley region during the October 2019 heatwave and forest fire event.

Part of the NEOSS Climate Risk project:
https://github.com/msovara/neoss-csir-chpc
"""

import streamlit as st
from pathlib import Path
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Risk Mapping Tool for Climate and Environmental Risks",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS - darker theme
st.markdown("""
    <style>
    .stApp, .main, [data-testid="stAppViewContainer"] {
        background-color: #1a1a2e;
    }
    .stApp > header {
        background-color: #16213e;
    }
    .main-header {
        font-size: 8rem;
        font-weight: bold;
        color: #e8e8e8;
        margin-bottom: 0.5rem;
        letter-spacing: 0.02em;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #a0a0b0;
        margin-bottom: 1.5rem;
    }
    .stImage img {
        border-radius: 8px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.3);
        max-width: 900px !important;
        width: auto !important;
        height: auto !important;
    }
    [data-testid="stSidebar"] {
        background-color: #16213e;
    }
    </style>
""", unsafe_allow_html=True)

# Paths
IMAGES_DIR = Path(__file__).parent / "images"
DATE_FORMAT = "%Y-%m-%d"

# Available dates (Oct 15-30, 2019)
AVAILABLE_DATES = [
    "2019-10-15", "2019-10-16", "2019-10-17", "2019-10-18", "2019-10-19",
    "2019-10-20", "2019-10-21", "2019-10-22", "2019-10-23", "2019-10-24",
    "2019-10-25", "2019-10-26", "2019-10-27", "2019-10-28", "2019-10-29",
    "2019-10-30",
]

# Exceedance map dates (Oct 15-23, 2019)
EXCEEDANCE_DATES = [
    "2019-10-15", "2019-10-16", "2019-10-17", "2019-10-18", "2019-10-19",
    "2019-10-20", "2019-10-21", "2019-10-22", "2019-10-23",
]


def get_image_path(date_str: str):
    """Get image path for a given date. Supports multiple naming conventions."""
    base_name = f"Nylsvley_WDIwrf_{date_str}"
    # Try simple name first (for deployed repo)
    simple_path = IMAGES_DIR / f"{base_name}.png"
    if simple_path.exists():
        return simple_path
    # Fallback: search for files containing the date
    for f in IMAGES_DIR.glob(f"*{date_str}*.png"):
        return f
    return None


def get_exceedance_path(date_str: str):
    """Get exceedance map path for a given date."""
    path = IMAGES_DIR / f"exceedance_{date_str}.png"
    return path if path.exists() else None


def get_fwi_path(date_str: str):
    """Get Fire Weather Index map path for a given date."""
    path = IMAGES_DIR / f"FWI_baseline_{date_str}.png"
    return path if path.exists() else None


def main():
    st.markdown('<p class="main-header">🌍 RISK MAPPING TOOL FOR CLIMATE AND ENVIRONMENTAL RISKS</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">October 2019 heatwave & forest fire case study</p>',
        unsafe_allow_html=True,
    )

    # Tabs
    tab_wdi, tab_exceedance, tab_fwi = st.tabs(["📊 Nylsvley WDI", "🔴 Exceedance Maps", "🔥 Fire Weather Index"])

    with tab_wdi:
        st.markdown("**Wetland Degradation Index (WDI)** — Nylsvley region")
        selected_date = st.selectbox(
            "Select date",
            options=AVAILABLE_DATES,
            index=0,
            format_func=lambda x: datetime.strptime(x, DATE_FORMAT).strftime("%d %B %Y"),
            key="wdi_date",
        )
        image_path = get_image_path(selected_date)
        if image_path and image_path.exists():
            st.subheader(f"Nylsvley - WDI {selected_date}")
            st.image(str(image_path), use_container_width=True)
        else:
            st.warning(
                f"Image not found for {selected_date}. "
                "Ensure the `images/` folder contains the WDI figures."
            )
        with st.expander("About WDI"):
            st.caption(
                "The Wetland Degradation Index indicates water deficit (blue) to surplus (red). "
                "Values range from -2.0 to 2.0. The black polygon outlines the Nylsvley region."
            )

    with tab_exceedance:
        st.markdown("**Exceedance Maps** — Southern Africa region")
        st.caption("Areas where environmental thresholds were exceeded (red dots)")
        # Filter to dates we have exceedance images for
        avail_exceedance = [d for d in EXCEEDANCE_DATES if get_exceedance_path(d)]
        if not avail_exceedance:
            avail_exceedance = EXCEEDANCE_DATES
        exc_date = st.selectbox(
            "Select date",
            options=avail_exceedance,
            index=0,
            format_func=lambda x: datetime.strptime(x, DATE_FORMAT).strftime("%d %B %Y"),
            key="exc_date",
        )
        exc_path = get_exceedance_path(exc_date)
        if exc_path and exc_path.exists():
            st.subheader(f"Exceedances at {exc_date}T12:00:00")
            st.image(str(exc_path), use_container_width=True)
        else:
            st.warning(f"Exceedance map not found for {exc_date}.")
        with st.expander("About Exceedances"):
            st.caption(
                "Exceedance maps show locations where certain environmental or weather thresholds "
                "were surpassed. Red dots indicate areas of elevated risk (e.g., heatwave, fire risk)."
            )

    with tab_fwi:
        st.markdown("**Fire Weather Index (FWI)** — Southern Africa region")
        st.caption("Fire risk indicator (0–300 scale: white = low, red/black = high)")
        avail_fwi = [d for d in AVAILABLE_DATES if get_fwi_path(d)]
        if not avail_fwi:
            avail_fwi = AVAILABLE_DATES
        fwi_date = st.selectbox(
            "Select date",
            options=avail_fwi,
            index=0,
            format_func=lambda x: datetime.strptime(x, DATE_FORMAT).strftime("%d %B %Y"),
            key="fwi_date",
        )
        fwi_path = get_fwi_path(fwi_date)
        if fwi_path and fwi_path.exists():
            st.subheader(f"Fire Weather Index (FWI) {fwi_date}")
            st.image(str(fwi_path), use_container_width=True)
        else:
            st.warning(f"FWI map not found for {fwi_date}.")
        with st.expander("About FWI"):
            st.caption(
                "The Fire Weather Index (FWI) indicates fire danger based on weather conditions. "
                "Values range from 0 (low risk) to 300 (extreme risk). "
                "Higher values (orange/red/black) indicate elevated fire weather conditions."
            )

    with st.sidebar:
        st.divider()
        st.markdown("[View on GitHub](https://github.com/msovara/neoss-csir-chpc)")


if __name__ == "__main__":
    main()
