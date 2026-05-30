# Frontier Tracking Log

> **Purpose:** Time-stamped log of literature searches, new discoveries, and tracking updates.
> **Update frequency:** Every 3–6 months, or upon significant new publication.
> **Search method:** Firecrawl web search + Google Scholar + IEEE Xplore + MDPI

---

## 2026-05-30: Initial Comprehensive Survey

### Search Performed
- Keywords: `"Contribution to the winding theory" "unified method" winding topology Mang Cai`
- Keywords: `"winding topology" unified method electrical machines 2017 2024 2025 2026`
- Keywords: `"winding function" "star of slots" winding factor harmonic analysis software tool 2020 2024`
- Keywords: `Baoyun Ge "Tensor Representation of Electric Machine Windings" ECCE 2024`
- Keywords: `"General, compact and easy-to-compute winding factor formulation" IET 2020`
- Keywords: `"Design of Electric Machine Windings to Independently Control Multiple Airgap Harmonics" 2023`
- Keywords: `"A General Approach to the Design of Multi-Layer Fractional-Slot Concentrated Windings" 2024`
- Keywords: `open source electric machine winding design python pyleecan femm`
- Keywords: `"Algorithmic Design of Modular Two-Layer Multiphase Windings" MDPI 2025`
- Keywords: `hairpin winding design optimization electric vehicle traction motor`
- Keywords: `multiphase winding design fractional slot concentrated winding harmonic mitigation`
- Keywords: `recent advances winding theory electrical machines review survey`

### Papers Found (New to Tracking)

| # | Paper | Year | Relevance |
|---|-------|------|-----------|
| 1 | Vann & Ge — Tensor Representation of Windings | 2024 | ★★★★★ |
| 2 | Ciriani et al. — General FSCW Design | 2024 | ★★★★★ |
| 3 | Gadiyar, Khamitov, Severson — Multi-Harmonic Control | 2023 | ★★★★☆ |
| 4 | Scuiller — Compact Winding Factor Formulation | 2020 | ★★★☆☆ |
| 5 | Khai et al. — Number Theory Winding Design | 2025 | ★★★☆☆ |
| 6 | Selema, Ibrahim, Sergeant — Winding Technology Review | 2022 | ★★★☆☆ |
| 7 | Lackner — Harmonic Scattering (Diploma) | 2022 | ★★☆☆☆ |

### Software Tools Found
- PyLecan (EOMYS) — Active, comprehensive
- SyR-e — Active, rotor-focused
- FEMM + pyFEMM — Mature, standard

### Key Insights
1. The unified method remains **unique** in providing a complete design-from-spectrum pipeline
2. The tensor method (Vann & Ge) is the closest parallel in ambition but addresses representation, not design
3. Hairpin winding is the dominant application driver since 2018
4. No published work has formally compared these methods

### Action Items from This Session
- [ ] Create `docs/research/` with literature survey, comparison, tracking log
- [ ] Add development roadmap
- [ ] Update root README with research tracking links
- [ ] Set up GitHub issue templates
- [ ] Schedule next search for 2026-09-01

---

## Next Scheduled Search

**Date:** 2026-09-01 (approximately)
**Focus areas:**
- Any new publications citing Cai (2017)
- Any new general winding design methods
- Advances in tensor representation (Vann & Ge follow-up)
- PyLecan winding module updates
- AI/ML applications to winding design

---

## How to Update This Log

When performing a new search:

1. Create a new `## YYYY-MM-DD` section
2. List all search queries used
3. List new papers found (with relevance rating)
4. Note any changes in the landscape
5. Update the "Action Items" list
6. Update the "Next Scheduled Search" date
