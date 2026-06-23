# WeEarth / TIA ↔ CSIR S2S Risk Mapping Tool ↔ LEDET

**Purpose:** Implementation mapping for proposals, LEDET briefings, and the 3‑month Space Hub pilot.  
**Companion:** `WEEARTH_SPACE_HUB_ALIGNMENT.md`

**Live prototype:** [Hazard Risk Mapping Tool](https://neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app)

---

## Implementation mapping table

| # | WeEarth / TIA implementation need | CSIR S2S risk mapping tool contribution | LEDET problem solved | Status / pilot deliverable |
|---|-----------------------------------|----------------------------------------|----------------------|----------------------------|
| **1** | **Ward-level environmental intelligence** to guide LEDET prioritisation | • High-resolution climate and environmental risk mapping for **heatwave**, **wildfire**, and **wetland degradation** (NWP + EO + ML hybrid)<br>• Oct 2019 Limpopo case study demonstrates event lifecycle (onset → peak → decay)<br>• Pilot: ward-level zonation and ranking layers for selected municipalities | Lack of spatially explicit evidence to prioritise vulnerable **wards and locations** for LEDET programmes and budgets | **Demonstrated** at research scale (3 km nest, site-specific wetlands); **ward aggregation = Month 2 pilot** |
| **2** | **Early warning information** that supports proactive intervention | • **Sub-seasonal to seasonal (S2S)** climate outlooks (2 weeks – 3 months)<br>• Early-warning products translated into **local risk escalation maps**<br>• **Event-based impact likelihood summaries** (e.g. fire occurrence probability by lead time)<br>• Web dashboard with date/lead selectors for officials | • Late or ineffective disaster preparedness<br>• High costs of emergency response and recovery<br>• Weak linkage between **climate forecasts and municipal action** | **Framework live** (S2S tabs); wildfire S2S prototype loaded; heatwave/wetland S2S folders ready; **scheduled refresh + escalation maps = pilot Months 1–2** |
| **3** | **Climate-resilient agricultural and land-use** decision support | • **Land degradation risk mapping** (wetland WDI deficit/surplus; future drought stress layers)<br>• S2S outlooks aligned to **land-preparation and planting windows**<br>• Integration path with **Farm Vision** spatial architecture | Increased vulnerability of **subsistence and smallholder farmers** to heat, drought, fire, and degraded land | **Wetland/heat/fire layers exist**; explicit **farm-scale land-degradation product = Month 3 pilot** |
| **4** | **Protection and rehabilitation of freshwater ecosystems** | • Spatial identification of **stressed wetlands** (EO–AI hybrid + NWP WDI)<br>• **Prioritisation maps** for rehabilitation (Nylsvley, Baleni, Khurini, Makuleke, Sekhukhune demonstrators)<br>• Time series of wetland stress through extreme events | • Declining water quality and ecosystem health<br>• **Weak targeting of rehabilitation investments** | **15 daily wetland maps** (Oct 2019) + WDI NWP layer in dashboard; **rehabilitation priority index = Month 3 pilot** |
| **5** | **Evidence-based disaster risk reduction** for human settlements | • **Heat and fire risk profiling** for vulnerable communities (Thabazimbi / Limpopo case study)<br>• Comparison of **NWP-only FWI** vs **EO–AI-enhanced** fire risk for realistic hotspot mapping<br>• Settlement-relevant summaries for planning and DRR plans | **Infrastructure failure** and community exposure during extreme heat and fire events | **Case study proven** (Oct 2019); **settlement overlay + vulnerability scoring = Month 2 pilot** |
| **6** | **Operational decision-support tools** for municipal officials | • **GIS-ready datasets** (standardised map catalogue, exportable rasters/vectors in pilot)<br>• **Dashboard** (NEOSS–CSIR–CHPC Hazard Risk Mapping Tool)<br>• **Technical briefs** translated for non-technical users (legends, info cards, plain-language summaries) | • **Limited technical capacity** at municipal level<br>• **Weak monitoring** of environmental interventions | **Dashboard deployed**; GIS export pack and **official brief templates = Month 1 pilot** |
| **7** | **Community engagement** supported by credible environmental evidence | • **Locally relevant maps and visuals** for ward-level engagement (daily sequences, hazard legends)<br>• Consistent branding with CSIR / LEDET / CHPC for trust and ownership<br>• Printable ward map packs for izimbizo and ward committees | **Low community ownership** of environmental programmes | **Visual assets exist**; **ward engagement pack + facilitator guide = Month 1–2 pilot** |
| **8** | *(Not numbered in source document — optional cross-cutting need)* | **Cross-agency data harmonisation:** SANSA EO, DWS water, DFFE biodiversity, NDA agriculture layers referenced in sidebar/metadata; Farm Vision spatial alignment | Siloed environmental data across provincial departments | **Named in programme design**; **formal data MOUs and layer registry = pilot governance task** |
| **9** | **Scalable, investment-ready environmental intelligence** | • **Repeatable analytical workflows** (WRF → indices → EO–ML → map catalogue → dashboard)<br>• **Documentation for replication** beyond pilot wards (methods, folder structure, training)<br>• **Investment-grade spatial evidence products** with metadata and QA<br>• ~**3-month pilot cycle** template for national scale-up (WeEarth / TIA model) | • Difficulty attracting **sustained funding and investment**<br>• **Pilot projects that fail to scale**<br>• **Weak long-term sustainability** of interventions | **GitHub repo + progress report + methods note exist**; **scaling playbook + investment brief = Month 3 pilot** |

---

## Column guide

| Column | Use in proposals |
|--------|------------------|
| **WeEarth / TIA need** | What the Space Hub / Farm Vision programme requires |
| **CSIR tool contribution** | What the hybrid NWP–EO–ML system actually delivers |
| **LEDET problem solved** | Provincial decision problem addressed |
| **Status / pilot deliverable** | Honest today vs what the 3‑month pilot completes |

---

## One-row summary per need (elevator pitch)

1. **Wards** — Turn national-scale climate science into **where** LEDET should act first.  
2. **Early warning** — Connect **2-week to 3-month outlooks** to **local escalation maps** officials can use before disasters.  
3. **Agriculture** — Link **land condition and S2S climate** to farmer and land-use decisions via Farm Vision.  
4. **Wetlands** — Show **which wetlands are stressed** and **where to rehabilitate** with spatial prioritisation.  
5. **Settlements** — Profile **heat and fire exposure** with evidence beyond weather-only indices.  
6. **Officials** — Give municipalities a **dashboard + GIS layers + plain briefs** without needing in-house modellers.  
7. **Communities** — Provide **credible local maps** that support ward engagement and programme ownership.  
8. **Integration** — Align hazard layers with **SANSA, DWS, DFFE, NDA** and Farm Vision spatial standards.  
9. **Scale** — Package a **repeatable 3-month pilot** that investors and TIA can replicate nationally.

---

## Copy-ready paragraph (LEDET / TIA cover text)

The CSIR Climate and Environmental Risk Mapping Tool directly addresses WeEarth Space Hub priorities by supplying high-resolution heatwave, wildfire, and wetland degradation intelligence; sub-seasonal to seasonal early-warning products translated into local risk maps; GIS-ready dashboards and datasets for municipal officials; ward-relevant visuals for community engagement; and documented, repeatable workflows for national scale-up. For LEDET, the tool closes the gap between climate forecasts and provincial action—providing spatial evidence to prioritise wards, target wetland rehabilitation, support climate-resilient agriculture through Farm Vision integration, and reduce the cost of reactive disaster response through proactive, map-based early warning.

---

*Last updated: June 2026*
