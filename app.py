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
    page_title="NEOSS Climate Risk - Nylsvley WDI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2rem;
        font-weight: bold;
        color: #0e1117;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #808495;
        margin-bottom: 1.5rem;
    }
    .stImage img {
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
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


def main():
    st.markdown('<p class="main-header">🌍 NEOSS Climate Risk</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Nylsvley Wetland Degradation Index (WDI) — October 2019 heatwave & forest fire case study</p>',
        unsafe_allow_html=True,
    )

    # Sidebar
    with st.sidebar:
        st.header("📅 Date Selection")
        selected_date = st.selectbox(
            "Select date",
            options=AVAILABLE_DATES,
            index=0,
            format_func=lambda x: datetime.strptime(x, DATE_FORMAT).strftime("%d %B %Y"),
        )
        st.divider()
        st.markdown("**About WDI**")
        st.caption(
            "The Wetland Degradation Index indicates water deficit (blue) to surplus (red). "
            "Values range from -2.0 to 2.0. The black polygon outlines the Nylsvley region."
        )
        st.divider()
        st.markdown("[View on GitHub](https://github.com/msovara/neoss-csir-chpc)")

    # Main content
    image_path = get_image_path(selected_date)

    if image_path and image_path.exists():
        st.subheader(f"Nylsvley - WDI {selected_date}")
        st.image(str(image_path), use_container_width=True)
    else:
        st.warning(
            f"Image not found for {selected_date}. "
            "Ensure the `images/` folder contains the WDI figures (e.g. `Nylsvley_WDIwrf_2019-10-15.png`)."
        )
        if IMAGES_DIR.exists():
            st.info(f"Files in images folder: {list(IMAGES_DIR.glob('*.png'))[:5]}...")
        else:
            st.info(f"Images directory not found: {IMAGES_DIR}")


if __name__ == "__main__":
    main()
