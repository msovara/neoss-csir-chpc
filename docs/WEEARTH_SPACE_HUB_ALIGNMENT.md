# WeEarth Space Hub & Farm Vision — Alignment with the CSIR Climate and Environmental Risk Mapping Tool

**Purpose:** Explain where the WeEarth / TIA implementation proposal sits in the broader NEOSS–CSIR–CHPC programme, what already exists, what the 3‑month pilot adds, and how outputs connect to LEDET and national partners.

**Related assets:**
- Live dashboard: [neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app](https://neoss-csir-chpc-apzmxmfm6s37cw5psdb6bn.streamlit.app)
- Source code: [github.com/msovara/neoss-csir-chpc](https://github.com/msovara/neoss-csir-chpc)
- Progress report: `PROJECT_PROGRESS_REPORT.md`

---

## 1. Where this document fits in the scheme of things

The WeEarth proposal is **not a separate science project**. It is the **operationalisation and municipal-scale delivery layer** on top of work already underway under NEOSS, CSIR climate and environmental risk research, and CHPC compute infrastructure.

Think of the programme in four stacked layers:

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 4 — WeEarth / Farm Vision / municipal uptake             │
│  Space hub · ward maps · GIS practitioner training · ~3 mo pilot│
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  LAYER 3 — Decision-support & dissemination                     │
│  NEOSS Hazard Risk Mapping Tool (Streamlit) · briefs · training │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  LAYER 2 — Hazard products (maps, indices, S2S outlooks)        │
│  WRF/FWI · EO–AI fire/wetland/heatwave · S2S wildfire prototypes│
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  LAYER 1 — Science & compute foundation                         │
│  WRF on CHPC · GEE/MODIS/VIIRS · ML (ConvLSTM, CNN, Anemoi)   │
└─────────────────────────────────────────────────────────────────┘
```

**WeEarth sits at Layer 4.** It defines *who* uses the tool (municipalities, GIS practitioners, Farm Vision), *how* products are embedded (space hub, ward-scale intelligence), and *what success looks like* in a 3‑month pilot (operational layers, training, scaling documentation).

**Layers 1–3 are largely built or in progress** through the CSIR risk mapping tool and NEOSS collaboration. The WeEarth document describes how to **anchor that capability in Limpopo (LEDET)** and scale it nationally with TIA’s preferred model.

---

## 2. One-sentence positioning

> The CSIR Climate and Environmental Risk Mapping Tool is the **technical engine** (NWP + EO + ML + HPC); the NEOSS web platform is the **prototype operational interface**; the WeEarth Space Hub proposal is the **municipality-anchored rollout and integration plan** that connects those outputs to Farm Vision, SANSA, DFFE, DWS, NDA, and ward-level decision-making.

---

## 3. Alignment with WeEarth priority areas

| WeEarth priority | CSIR risk mapping tool response | Current status |
|------------------|----------------------------------|----------------|
| Disaster risk & climate monitoring (flood, drought, fire, wetlands, land degradation) | Hybrid NWP + EO + ML framework; demonstrated for **heatwave, wildfire, wetland degradation** (Oct 2019 Limpopo case study) | **Pilot-proven** for three hazards; flood/drought S2S layers not yet in dashboard |
| GIS and space-enabled risk products | Georeferenced PNG map catalogue; GIS-ready naming; WRF domains; EO from MODIS/VIIRS via GEE | **Available** as exportable layers; formal GeoTIFF/Shapefile pipeline for Farm Vision = **pilot Month 1 task** |
| Municipal- and village-scale risk products | 3 km WRF nest; wetland sites (Nylsvley, Baleni, etc.); Thabazimbi fire case study | **Research scale demonstrated**; systematic **ward-level** aggregation = **pilot scope** |
| Early warning for agriculture, water, infrastructure, livelihoods | S2S tabs (2 wk–3 mo); event lifecycle (onset → peak → decay) shown in Oct 2019 replay | **Framework live**; S2S heatwave/wetland PNGs pending; wildfire S2S prototype exists (May 2026 init) |
| Operational outputs | Streamlit dashboard; CHPC job workflows; repeatable map folders | **Prototype operational** (case-study replay + selective S2S); not yet automated real-time warning |

| WeEarth implementation model | How the CSIR tool aligns |
|------------------------------|---------------------------|
| Space-hub-based | Dashboard + map assets can be embedded in hub GIS workflows (Month 1 integration) |
| Municipality anchored | LEDET logo/branding already on platform; Limpopo case study is geographically aligned |
| Driven by GIS practitioners | Static map viewer + date/lead selectors; training materials = **pilot deliverable** |
| Integration with Farm Vision, SANSA, DFFE, DWS, NDA | Tool provides ** hazard layers** Farm Vision can consume; cross-agency links = **governance + data-sharing pilot work** |
| ~3 month cycle pilots | Matches proposed Month 1–3 table in WeEarth doc |
| Training, dashboards, maps, actionable intelligence | Streamlit = dashboard prototype; maps exist; training pack = **to be written in pilot** |

---

## 4. Mapping WeEarth implementation needs → CSIR tool → LEDET value

| # | WeEarth / TIA need | CSIR S2S risk tool contribution | LEDET problem addressed |
|---|-------------------|----------------------------------|-------------------------|
| 1 | Ward-level environmental intelligence | High-res heatwave, fire, wetland layers; ward zonation in pilot Month 2 | Prioritise vulnerable wards with spatial evidence |
| 2 | Early warning → proactive intervention | S2S outlooks + local risk escalation maps; event summaries | Bridge climate forecasts and municipal action |
| 3 | Climate-resilient agriculture & land use | Land degradation / wetland stress maps; future drought layers | Support smallholder and subsistence farmer decisions |
| 4 | Freshwater ecosystem protection | Wetland WDI + EO–AI hybrid maps; rehabilitation prioritisation | Target rehabilitation investments |
| 5 | DRR for human settlements | Heat and fire profiling (Oct 2019 demonstrated) | Reduce infrastructure and community exposure |
| 6 | Operational tools for officials | Streamlit dashboard + GIS-ready exports + plain-language briefs | Build capacity where technical staff are limited |
| 7 | Community engagement with credible evidence | Local maps for ward meetings | Increase programme ownership |
| 9 | Scalable, investment-ready intelligence | Repeatable HPC + ML + map catalogue workflow; documentation | Move beyond one-off pilots |

**Key message for proposals:** Rows 1–7 are **partially satisfied today** by the research prototype (Layer 3). The WeEarth pilot **closes the gap** between prototype and municipality-ready operations (Layer 4).

---

## 5. What already exists vs what the 3‑month pilot adds

### Already in place (research → prototype operations)

| Component | Description |
|-----------|-------------|
| **Science case study** | Oct 2019 Limpopo heatwave & fire; WRF → FWI; EO–AI fire risk (ConvLSTM); wetland WDI; heatwave CNN maps |
| **Web platform** | NEOSS–CSIR–CHPC Hazard Risk Mapping Tool (four tabs: case study + three S2S hazards) |
| **Branding & partners** | CSIR, NICIS/CHPC, LEDET logos on dashboard |
| **HPC foundation** | WRF workflows on Lengau; ML infrastructure tests (Anemoi/JRA-3Q — parallel atmospheric ML track) |
| **Publication pathway** | Mulovhedzi & Sovara abstract on EO–AI fire risk + platform dissemination |
| **S2S wildfire prototype** | Five fire-occurrence probability maps (May 2026 initialisation) in app |

### Added by WeEarth 3‑month pilot (operationalisation)

| Month | WeEarth activity | Fills which gap |
|-------|------------------|-----------------|
| **Month 1** | Baseline hazard layers into Farm Vision / Space Hub; training datasets; technical reports | GIS export formats; hub integration; practitioner training pack |
| **Month 2** | Municipal/district S2S products; local-scale mapping | Ward aggregation; scheduled S2S refresh; district focus areas |
| **Month 3** | Land prep & rehabilitation intelligence; scaling documentation | Investment-ready replication guide; cross-department briefs |

---

## 6. Relationship to other programme threads

| Thread | Role relative to WeEarth |
|--------|---------------------------|
| **NEOSS programme** | Umbrella funding and collaboration frame; WeEarth is a **delivery channel** into provincial and TIA space-hub networks |
| **CHPC Lengau** | Runs heavy WRF and ML training jobs; WeEarth does not replace HPC — it **consumes** scheduled map outputs |
| **LEDET** | Primary provincial anchor; Oct 2019 case study geography; municipal pilot partner |
| **Patience Mulovhedzi fire EO–AI work** | Supplies **Layer 2** fire science (FWI vs ConvLSTM); WeEarth packages it for officials |
| **Anemoi / JRA-3Q on Lengau** | **Future S2S atmospheric backbone** — not yet feeding live dashboard maps; long-term complement to WRF+EO stack |
| **Farm Vision** | Spatial architecture and agricultural user base; receives hazard layers from Month 1 integration |
| **SANSA, DFFE, DWS, NDA** | Data providers, policy alignment, and co-beneficiaries; WeEarth doc names them as integration partners |

---

## 7. Honest capability statement (for proposals and reports)

Use this wording to stay accurate:

> The CSIR Climate and Environmental Risk Mapping Tool has **demonstrated** integrated heatwave, wildfire, and wetland degradation risk mapping for a high-impact Limpopo case study, with sub-seasonal wildfire forecast prototypes and a live web dashboard. It provides a **credible foundation** for WeEarth Space Hub deployment but is **not yet** a fully automated national early-warning system. The proposed 3‑month pilot converts research outputs into **ward-relevant, GIS-integrated, training-supported operational products** aligned with Farm Vision and LEDET priorities.

**Avoid over-claiming:**
- Do not state that all ML training ran on CHPC unless confirmed per model.
- Do not state real-time warning until scheduled ingest and refresh are operational.
- Do not imply flood/drought layers are live in the dashboard unless added.

---

## 8. Suggested narrative for proposals (copy-ready)

**Problem:** Limpopo faces rising heat, fire, wetland stress, and drought/flood variability, but municipal officials lack spatially explicit, forecast-linked intelligence at ward scale.

**Solution:** Deploy the CSIR hybrid NWP–EO–ML risk mapping tool through a WeEarth Space Hub pilot: integrate baseline hazard layers with Farm Vision, produce municipal S2S early-warning maps, train GIS practitioners, and document a repeatable 3‑month cycle for national scale-up.

**Evidence it works:** October 2019 case study captured event onset, intensification, peak, and decay; EO–AI fire maps outperformed FWI-only products spatially; dashboard already hosts case-study and S2S prototype layers for stakeholder review.

**Ask:** Month 1–3 pilot resourcing for hub integration, ward products, training, and scaling documentation — building on existing CSIR, CHPC, and LEDET collaboration.

---

## 9. Quick reference — document hierarchy

| Document / asset | Layer | Audience |
|------------------|-------|----------|
| WeEarth Space Hub proposal (this alignment source) | 4 — Rollout | TIA, LEDET, municipal GIS, Farm Vision |
| `WEEARTH_SPACE_HUB_ALIGNMENT.md` (this file) | Meta — Programme map | Internal CSIR / CHPC / proposal writers |
| `PROJECT_PROGRESS_REPORT.md` | 3 — Platform status | NEOSS, reviewers, partners |
| Fire EO–AI abstract (Mulovhedzi & Sovara) | 2 — Science evidence | Conference / journal |
| Streamlit app | 3 — Prototype ops | Stakeholders, demos |
| Anemoi/Lengau training notes | 1 — Future S2S ML | Technical / HPC |

---

*Last updated: June 2026*
