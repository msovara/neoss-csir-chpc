# NEOSS Climate Risk

[![GitHub](https://img.shields.io/badge/GitHub-neoss--csir--chpc-blue)](https://github.com/msovara/neoss-csir-chpc)

## PROJECT OVERVIEW

This project seeks to develop an innovative, AI-powered monitoring and risk-mapping tool tailored to severe weather and environmental hazards at sub-seasonal to seasonal (S2S) time scales, spanning two weeks to three months ahead. By integrating Earth Observation (EO) data from space-based, aerial, and in-situ sources with advanced machine learning techniques and numerical weather and climate models, the project aims to significantly improve the early detection and prediction of extreme weather and environmental hazard probabilities and hotspots.

The tool will serve as a strategic resource for enhancing South Africa's disaster risk preparedness, climate change adaptation, and evidence-based policy formulation. Emphasis is placed on detecting and mapping the probability of extreme weather events such as heatwaves, wetland degradation and fire risk, thereby enabling timely, actionable insights to safeguard communities, ecosystems, and infrastructure.

The project further promotes multidisciplinary collaboration and knowledge exchange among scientists, government entities, civil society, and community-based structures. It encourages the use of both public and private EO datasets to improve data accessibility and literacy, while fostering inclusive participation to address socio-economic vulnerabilities and promote equitable resilience across all regions.

---

## CURRENT DELIVERABLES

- **Model simulation for a case study** — Heatwave event coupled with forest fires over parts of the study domain. The model simulation was done for both:
  - **Medium range**: up to 16-days forecast period (resource-effective case study setup)
  - **S2S time scale**: up to 90 days (for implementation of operational forecasts)
  - This event is believed to have impacted wetlands in the region.

- **Integration of EO datasets and application of AI techniques**

- **Risk mapping techniques**

- **Construction of mapping tool and distribution platform**

- **Collaboration opportunities and collaborator platform for warning distribution**

---

## WDI VISUALIZATION APP

An interactive Streamlit app visualizes the **Wetland Degradation Index (WDI)** for the Nylsvley region during the October 2019 heatwave and forest fire case study. The app displays daily WDI spatial maps from 15–30 October 2019.

### Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy on Streamlit Community Cloud (free)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select repository: `msovara/neoss-csir-chpc`
5. Branch: `main`
6. Main file path: `app.py`
7. Click **"Deploy"**

Your app will be live at `https://<your-app-name>.streamlit.app` within a few minutes.

---

## REPOSITORY

**URL:** [https://github.com/msovara/neoss-csir-chpc](https://github.com/msovara/neoss-csir-chpc)
