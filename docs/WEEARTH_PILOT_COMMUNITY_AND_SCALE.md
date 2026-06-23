# WeEarth Pilot — Community Engagement, Scale-Up & 3‑Month Implementation Scope

**Focus:** Implementation needs **#7** (community engagement) and **#9** (scalable, investment-ready intelligence), plus the full **3‑month pilot** plan with activities, outcomes, and deliverables.

**Related:** `WEEARTH_TIA_LEDET_MAPPING.md` · `WEEARTH_SPACE_HUB_ALIGNMENT.md`  
**Prototype:** [Hazard Risk Mapping Tool](https://neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app)

---

## Need #7 — Community engagement supported by credible environmental evidence

### WeEarth / TIA requirement

- Locally relevant maps and visuals for **ward-level engagement**

### LEDET problem

- **Low community ownership** of environmental programmes — communities disengage when messages are generic, technical, or not tied to places they know

### CSIR S2S risk mapping tool contribution

| Contribution | Description |
|--------------|-------------|
| **Place-based hazard visuals** | Daily heatwave, fire, and wetland maps for Limpopo (Oct 2019 case study proves format; pilot produces **current ward clips**) |
| **Plain-language legends** | Colour scales and risk categories already in dashboard info cards — adapted for **isiNothern Sotho / Sepedi summaries** in engagement pack |
| **Before / during / after sequences** | Event lifecycle maps show *why* a heatwave or fire week mattered — supports storytelling in ward izimbizo |
| **Trusted branding** | CSIR + LEDET + CHPC logos on outputs signal **credible science**, not ad hoc graphics |
| **Print-ready ward packs** | A4/PDF map sets per ward: “Your ward this season — heat, fire, wetland stress” |
| **Facilitator guide** | Short script for LEDET environmental officers: how to read maps, lead discussion, link to local action |

### What exists today vs pilot

| Today | Pilot completes |
|-------|-----------------|
| Case-study maps viewable in Streamlit | **Ward-clipped** map packs for 2–3 pilot municipalities |
| English info cards and legends | **Community briefing sheets** (plain language + local place names) |
| Demo-ready for officials | **Engagement toolkit**: prints, slides, facilitator guide, feedback form |

### Success indicator for LEDET

> Ward committees can point to **their area on a map**, understand **what risk means for them**, and identify **one local action** (e.g. fire belt, wetland buffer, heat shelter) supported by the same evidence officials use.

---

## Need #9 — Scalable, investment-ready environmental intelligence

### WeEarth / TIA requirement

- Repeatable analytical workflows  
- Documentation for replication beyond pilot wards  
- Investment-grade spatial evidence products  

### LEDET problems

- Difficulty attracting **sustained funding and investment**  
- **Pilot projects that fail to scale**  
- **Weak long-term sustainability** of interventions  

### CSIR S2S risk mapping tool contribution

| Contribution | Description |
|--------------|-------------|
| **Repeatable workflow** | Standard pipeline: NWP (WRF) → hazard indices (FWI, WDI, heat exceedance) → EO–ML enhancement → map catalogue → dashboard / GIS export |
| **Standard folder & naming** | `images/case_study/` and `images/forecasts/` structure — any new ward or district reuses the same ingest pattern |
| **Metadata & QA** | Each product: date, hazard type, source (NWP / EO / ML), resolution, lead time — **investment-grade spatial evidence** for auditors and donors |
| **Open methods documentation** | GitHub repo, progress report, methods note — supports **replication beyond pilot wards** |
| **3‑month pilot template** | Documented cycle (baseline → municipal scale → rehab/ag scale + scaling report) for **TIA national roll-out** |
| **CHPC + web architecture** | Heavy compute on Lengau; lightweight Streamlit / Farm Vision front end — **sustainable ops model** (refresh maps on schedule, not rebuild from scratch) |

### What exists today vs pilot

| Today | Pilot completes |
|-------|-----------------|
| Research prototype + live dashboard | **Operations runbook** (who refreshes maps, how often, where stored) |
| GitHub + progress report | **Scaling playbook** — replicate in a new municipality in ≤3 months |
| Oct 2019 case study as proof | **Investment brief** — costed pathway from pilot → provincial → national |

### Success indicator for TIA / investors

> A second municipality (or ward cluster) can be onboarded using **written procedures and training materials only**, without redesigning the science stack — and donors receive **auditable map products with metadata**.

---

## 3‑Month pilot implementation scope (expanded)

### Overview

| Month | Theme | Primary needs addressed |
|-------|--------|-------------------------|
| **1** | Baseline integration & training foundation | 2, 6, **7**, **9**, Farm Vision alignment |
| **2** | Municipal / district operational products | 1, 2, 5, **7** |
| **3** | Agriculture, rehabilitation & scale-out | 3, 4, **9** |

---

### Month 1 — Integration of baseline hazard layers

**Activities**

1. Export operational **heatwave**, **wildfire**, and **land degradation / wetland stress** layers (GeoTIFF/Shapefile + PNG) from existing map catalogue  
2. Ingest baseline layers into **Farm Vision / Space Hub** GIS workflows (coordinate system, layer registry, symbology)  
3. Load **sub-seasonal early warning** prototype layers (wildfire S2S; heatwave/wetland as available)  
4. Develop **training-ready geospatial datasets** (sample wards, metadata, README)  
5. Draft **technical reports** for municipal planning and investment readiness  
6. Confirm **alignment with Farm Vision spatial architecture** (layer IDs, APIs or file drop protocol)  
7. Develop **training materials for GIS practitioners** (half-day module + exercises)  
8. Start **community engagement pack** (template ward map, legend card, facilitator outline) — **Need #7**

**Outcomes**

| Outcome | Deliverable |
|---------|-------------|
| Operational heatwave, wildfire, land degradation risk maps | Baseline GIS layer package + dashboard refresh |
| Sub-seasonal early warning products | S2S layers in hub + app (≥1 hazard live on schedule) |
| Climate-risk layers in Farm Vision / Space Hub | Signed integration checklist |
| Training-ready geospatial datasets | Zip bundle + data dictionary |
| Technical reports for planning / investment | Report v1: methods, coverage, limitations |
| Farm Vision spatial alignment | Layer schema document |
| Training material for GIS practitioners | Slides + hands-on workbook |
| Workflow documentation started | Folder structure + ingest SOP — **Need #9** |

---

### Month 2 — Municipal and local-scale risk mapping

**Activities**

1. Produce **municipal- and ward-scale** heat, fire, and wetland layers for **selected districts**  
2. Generate **S2S early warning products** with district focus (escalation maps: normal → elevated → high)  
3. Add **settlement / infrastructure exposure** overlays where data allow — Need #5  
4. Run **GIS practitioner training** (cohort 1) using Month 1 materials  
5. Pilot **ward engagement sessions** with printed map packs and facilitator guide — **Need #7**  
6. Collect official feedback for dashboard and brief templates — Need #6  

**Outcomes**

| Outcome | Deliverable |
|---------|-------------|
| Municipal and local-scale risk mapping | Ward-ranked priority maps for pilot municipalities |
| S2S early warning for selected districts | District escalation maps + 1-page official brief per init date |
| Community engagement tested | ≥2 ward sessions; feedback summary |
| Municipal uptake | LEDET / municipality sign-off on map usability |

---

### Month 3 — Refined intelligence, rehabilitation & scaling

**Activities**

1. **Land preparation** risk layers (S2S climate + degradation) for Farm Vision agricultural windows — Need #3  
2. **Wetland rehabilitation prioritisation** maps — Need #4  
3. Final **decision-support products** for municipalities and departments (integrated briefs)  
4. Complete **documentation and scaling recommendations** — **Need #9**  
5. **Investment brief** and **3‑month replication playbook** for TIA  
6. Final GIS practitioner training (cohort 2) and **train-the-trainer** handover  

**Outcomes**

| Outcome | Deliverable |
|---------|-------------|
| Refined risk intelligence for land preparation | Ag-season map series + Farm Vision layer |
| Rehabilitation decision support | Wetland priority map + intervention shortlist |
| Decision-support products | Municipal + departmental brief pack (PDF) |
| Documentation & scaling | Scaling playbook, ops runbook, investment brief |
| Sustainability | Named LEDET / hub owner for map refresh cadence |

---

## Master table — timeframe, activity, outcome

| Timeframe | Activity | Outcome |
|-----------|----------|---------|
| **Month 1** | Integration of baseline hazard layers | Operational heatwave, wildfire, and land degradation risk maps |
| | | Sub-seasonal early warning products in hub and dashboard |
| | | Climate-risk layers integrated into Farm Vision / Space Hub workflows |
| | | Training-ready geospatial datasets |
| | | Technical reports supporting municipal planning and investment readiness |
| | | Alignment with Farm Vision spatial architecture |
| | | Training material development for GIS practitioners |
| | | Community engagement templates and workflow SOP (Needs **7**, **9**) |
| **Month 2** | Municipal and local-scale risk mapping | Ward- and district-scale priority maps |
| | S2S early warning for selected districts | Escalation maps linked to municipal action |
| | Ward engagement pilot | Credible local visuals; ownership feedback (Need **7**) |
| **Month 3** | Refined risk intelligence for land preparation and rehabilitation | Ag and wetland rehab decision-support products |
| | Decision-support products for municipalities and departments | Integrated official briefs |
| | Documentation and scaling recommendations | Replication playbook + investment brief (Need **9**) |

---

## How Needs #7 and #9 thread through the pilot

```
Month 1                          Month 2                          Month 3
────────────────────────────────────────────────────────────────────────────
Need #7: Templates &             Need #7: Ward sessions &         Need #7: Refined packs
         branding                         feedback loop                    + train-the-trainer

Need #9: SOP + layer schema       Need #9: Municipal proof         Need #9: Playbook +
         + metadata                       of repeatability                 investment brief
```

---

## Copy-ready text — Needs #7 & #9 (proposal insert)

**Community engagement (#7).** The pilot will produce ward-clipped map packs, plain-language legend cards, and a facilitator guide so LEDET and ward committees can discuss heat, fire, and wetland risk using the same credible spatial evidence as provincial officials. By grounding programmes in locally recognisable places rather than generic climate messages, the tool supports stronger community ownership of environmental interventions.

**Scalable intelligence (#9).** The CSIR workflow — from NWP and EO–ML map generation through a standardised catalogue to dashboard and Farm Vision integration — will be documented as a repeatable 3‑month pilot template. Metadata-rich, investment-grade spatial products, an operations runbook, and a scaling playbook will allow TIA and partners to replicate the approach in additional municipalities without rebuilding the science stack, improving sustainability and donor confidence.

---

## Copy-ready text — 3‑month pilot (executive summary)

Over three months, the pilot will (1) integrate baseline heatwave, wildfire, and land-degradation layers and sub-seasonal early-warning products into Farm Vision and the Space Hub; (2) downscale products to selected municipalities and wards with GIS practitioner training and community engagement sessions; and (3) deliver land-preparation and wetland-rehabilitation decision-support maps, municipal briefs, and scaling documentation for provincial and national roll-out. Each month produces operational outputs — not slide decks alone — aligned with WeEarth’s space-hub, municipality-anchored, GIS-driven implementation model.

---

*Last updated: June 2026*
