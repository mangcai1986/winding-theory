# Literature Survey: Winding Topology Theory & Design

> **Last comprehensive search:** 2026-05-30
> **Next scheduled search:** 2026-09-01
> **Search method:** Firecrawl web search + direct paper access

This document categorizes and summarizes all known related work since the publication of Mang Cai's unified winding topology method (2016/2017). Each entry is tagged with its relation to the unified method.

---

## Category A: Directly Comparable Unified/General Methods

Methods that aim to provide a general framework for winding analysis or design (most relevant to the unified method).

### A1. Tensor Representation of Electric Machine Windings (ECCE 2024)
| Field | Detail |
|-------|--------|
| **Authors** | J. Dillon Vann, Baoyun Ge |
| **Affiliation** | University of Florida / Georgia Institute of Technology |
| **Venue** | IEEE Energy Conversion Congress & Exposition (ECCE) 2024 |
| **Link** | [NSF PAR](https://par.nsf.gov/servlets/purl/10556474) |
| **Status** | Published, ongoing work |

**Core idea:** Represent winding topology using rank-2 (C₁, C₂) and rank-3 tensors. C₁ encodes coil-side-to-slot mapping; C₂ encodes coil-to-phase connections. The product C₁·C₂ yields the differential of the winding function.

**Covered winding types:** Fractional-slot, full-pitch, short-pitch, concentric, hairpin (rank-3 for layers).

**Relation to unified method:**
- **Complementary approach**: Tensor method = bottom-up representation (slot diagram → tensors → winding function); unified method = top-down design (ideal spectrum → symmetries → winding)
- The tensor method does **not** solve the inverse problem (from ideal harmonics to winding configuration) — which is the core strength of the unified method
- The tensor method's "future work" section explicitly states: *"design algorithms that can efficiently explore high-performance winding configurations... convert the winding exploration problem into an exact cover problem"* — this aligns with the unified method's design pipeline

**Key citation:** G. Kron, "Tensor Analysis of Networks" (1949) — the tensor method traces its roots here, not directly to Cai's work.

### A2. General Approach to Multi-Layer FSCW Design (IEEE Access 2024)
| Field | Detail |
|-------|--------|
| **Authors** | Cesare Ciriani, Hamid Ali Khan, Alberto Tessarolo et al. |
| **Affiliation** | University of Trieste, Italy |
| **Venue** | IEEE Access, vol. 12, 2024 |
| **Link** | [ResearchGate](https://www.researchgate.net/publication/381686242) |

**Core idea:** A general design method for multi-layer fractional-slot concentrated windings (FSCW) with arbitrary numbers of slots, poles, and phases. Uses winding vector definitions and phase current identification.

**Relation to unified method:**
- **Most similar in scope** among all surveyed works — both aim for generality across slot/pole/phase combinations
- The unified method covers **more winding types** (integer slot, over-harmonic, multi-turn, multi-coil, multi-conductor), not just FSCW
- The unified method has a **complete design pipeline** (ideal spectrum → MMF → multi-phase → single-phase → coil group → coils); Ciriani et al. focus on multi-layer FSCW only
- The unified method's **symmetry-based approach** is conceptually distinct from their winding-vector approach

### A3. Independent Control of Multiple Airgap Harmonics (IEEE TIA 2023)
| Field | Detail |
|-------|--------|
| **Authors** | F. Nishanth Gadiyar, Anvar Khamitov, Eric L. Severson |
| **Affiliation** | University of Wisconsin-Madison |
| **Venue** | IEEE Trans. on Industry Applications, 2023 (also ECCE 2023) |
| **Link** | [IEEE](https://ieeexplore.ieee.org/document/10313586/) |

**Core idea:** Design windings that independently control multiple airgap field harmonics — critical for bearingless motors, harmonic-biased machines, and multi-harmonic torque production.

**Relation to unified method:**
- Directly relevant to the unified method's **harmonic spectrum analysis** capability
- The unified method can analyze which harmonics a winding produces; Severson's method designs for **intentional multi-harmonic use**
- Potential integration: use the unified method's symmetry framework to **design** windings that achieve Severson's multi-harmonic targets

---

## Category B: Winding Factor & Harmonic Analysis

### B1. General, Compact Winding Factor Formulation (IET EPA 2020)
| Field | Detail |
|-------|--------|
| **Authors** | Franck Scuiller |
| **Affiliation** | École Navale, France |
| **Venue** | IET Electric Power Applications, vol. 14(8), 2020 |
| **Link** | [IET](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-epa.2019.0950) |

**Core idea:** A compact algebraic winding factor formulation that is easier to compute than traditional star-of-slots methods.

**Relation to unified method:**
- The unified method's DFT-like transformation (`winding_topology_to_spectrum`) is a different mathematical approach to the same problem
- Scuiller's formulation is more **compact**; the unified method's approach is more **general** (handles arbitrary connection matrices, not just standard layouts)

### B2. Winding Function Approach for Winding Analysis
| Field | Detail |
|-------|--------|
| **Authors** | Multiple |
| **Venue** | IEEE Trans. Magnetics / Industry Applications, various years |

A long-established approach using winding functions for inductance calculation and MMF analysis. While not new (Lipo, Novotny, etc.), refinements continue.

**Relation to unified method:**
- The unified method's `get_mmf()` and `winding_topology_to_spectrum()` are consistent with winding function theory
- The unified method adds the **symmetry-based design pipeline** that classical winding function theory lacks

### B3. Harmonic Scattering of Multi-Phase Windings (TU Wien 2022)
| Field | Detail |
|-------|--------|
| **Authors** | David Alexander Lackner |
| **Affiliation** | TU Wien (Diploma thesis) |
| **Link** | [TU Wien Repositorium](https://repositum.tuwien.at/handle/20.500.12708/20229) |

**Core idea:** Mathematical formulation of harmonic scattering in poly-phase integer and fractional slot windings.

---

## Category C: Algorithmic & Automated Winding Design

### C1. Algorithmic Design of Modular Two-Layer Multiphase Windings (Energies 2025)
| Field | Detail |
|-------|--------|
| **Authors** | Mykhailo Khai, Bohdan Kharchyshyn, Oleksandr Makarchuk et al. |
| **Venue** | Energies, vol. 18(23), 6320, 2025 |
| **Link** | [MDPI](https://www.mdpi.com/1996-1073/18/23/6320) |

**Core idea:** Using number theory (GCD, modular arithmetic) to algorithmically construct winding diagrams for modular two-layer multiphase windings.

**Relation to unified method:**
- Purely **algebraic** approach vs. the unified method's **symmetry-based** approach
- Limited to two-layer windings; the unified method handles single-layer, multi-layer, multi-turn, etc.
- The algebraic approach may be **more computationally efficient** for specific cases

### C2. Electrical Machine Winding Performance Optimization by Multi-Objective PSO
| Field | Detail |
|-------|--------|
| **Year** | 2024 |
| **Method** | Particle Swarm Optimization for MMF and end-winding leakage |

**Relation to unified method:**
- The unified method could provide the **evaluation function** (winding factor spectrum) for such optimization
- Potential integration: use the unified method's design pipeline as the **forward model** inside an optimization loop

### C3. Automated AC Winding Design (ResearchGate)
| Field | Detail |
|-------|--------|
| **Authors** | Various |
| **Year** | Multiple (classical problem) |

The star-of-slots method remains the most widespread design tool, but automated approaches have been explored since at least the 1990s.

---

## Category D: Application-Specific Winding Developments

### D1. Hairpin Winding Design (2018–2025)
| Year | Contribution | Key Reference |
|------|-------------|---------------|
| 2018 | Analytical approach to hairpin winding design | Bianchi & Berardi, ECCE 2018 |
| 2022 | Comprehensive design guideline for EV traction | Zou et al., IEEE TTE |
| 2024 | Continuous hairpin winding for multi-phase MW-class aircraft propulsion | Yang & Gerada |
| 2025 | Thermal management of hairpin windings | Various |
| 2025 | Reliability-oriented design | IEEE TTE |

**Relation to unified method:**
- Hairpin windings are **multi-layer windings** — the unified method's multi-layer derivation (`obtain_multi_layer_winding_topology`) is directly applicable
- A dedicated `examples/hairpin_winding.py` would demonstrate the unified method's relevance to this hot topic

### D2. Multiphase Fault-Tolerant Windings for Aerospace (2020–2025)
- Fault-tolerant multi-phase machines for electric aircraft propulsion
- Dual three-phase, six-phase, nine-phase configurations
- Modular stator designs for fault isolation

**Relation to unified method:**
- The unified method handles **arbitrary phase numbers** (not just 3-phase)
- Multi-phase symmetry detection is a core capability

### D3. Field-Modulated / Vernier Machines
- Dual-stator, flux-modulated PM machines for high torque density
- Utilize multiple working harmonics intentionally
- Winding topology critical for harmonic utilization

---

## Category E: Open-Source Software Tools

### E1. PyLecan (2018–present)
| Field | Detail |
|-------|--------|
| **Project** | PYthon Library for Electrical Engineering Computational Analysis |
| **Organization** | EOMYS |
| **Repository** | [github.com/Eomys/pyleecan](https://github.com/Eomys/pyleecan) |
| **Status** | Active development, multiple releases |

**Capabilities:** Multi-physics design and optimization of electrical machines. Includes winding definition, FEMM coupling, magnetic/thermal/mechanical simulation.

**Relation to unified method:**
- PyLecan has winding definition but **no symmetry-based design pipeline**
- **Integration opportunity**: Export unified method winding designs to PyLecan for FEA validation
- **Differentiation**: The unified method provides analytical insight that PyLecan's numerical approach cannot match for winding topology design

### E2. SyR-e (2018–present)
| Field | Detail |
|-------|--------|
| **Project** | Synchronous Reluctance motor design |
| **Focus** | Rotor topology optimization |

Less relevant for winding topology, but complementary for complete machine design.

### E3. FEMM (Finite Element Method Magnetics)
| Field | Detail |
|-------|--------|
| **Status** | Mature, widely used |
| **Python binding** | `pyFEMM` |

Standard open-source FEA tool. Useful for **validating** winding designs produced by the unified method.

---

## Category F: AI/ML for Winding Design (2024–2025)

Emerging trend with potential for significant impact:

- **AI data-driven framework for optimal electrical machine design** (IEEE Access 2025)
- **Machine learning meta-modeling** for FEA acceleration
- **Genetic algorithm-based winding optimization** (ICREPQ 2025)
- **Comprehensive review of sustainable electrical machine technologies** (Archives of Computational Methods in Engineering, 2026)

**Relation to unified method:**
- The unified method's **deterministic, analytical nature** is complementary to data-driven approaches
- The unified method can serve as a **fast analytical surrogate** within ML optimization loops
- **Training data generation**: The unified method can generate large datasets of winding topologies with known properties for ML training

---

## Method Classification Matrix

| Method | Type | Winding Types | Phase Count | Design or Analysis | Generality |
|--------|------|--------------|-------------|-------------------|------------|
| **Cai (2017) Unified Method** | Symmetry-based | All | Arbitrary | **Both** | ★★★★★ |
| Vann & Ge (2024) Tensor | Tensor algebra | 5 types | 3-phase | Analysis | ★★★☆☆ |
| Ciriani et al. (2024) FSCW | Winding vector | Multi-layer FSCW | Arbitrary | Design | ★★★☆☆ |
| Scuiller (2020) Winding Factor | Algebraic | Standard | 3-phase | Analysis | ★★☆☆☆ |
| Khai et al. (2025) Number Theory | Algebraic | Two-layer modular | Multiphase | Design | ★★★☆☆ |
| Severson et al. (2023) Multi-Harmonic | Optimization | Custom | Multiphase | Design | ★★★★☆ |
| PyLecan | Numerical FEA | Any | Any | Analysis | ★★★★☆ |

> **Key insight:** The unified method (Cai 2017) remains the **only** method that provides both a complete **analysis** (spectrum, symmetries) and **design** (from ideal spectrum to realizable winding) pipeline in a single unified framework. No other method covers all winding types (integer slot, fractional slot, single-layer, double-layer, multi-layer, multi-turn, multi-coil, multi-conductor, over-harmonic) in one system.

---

## References

1. M. Cai, "Contribution to the winding theory: Introduction of a unified method for the treatment of winding topology," PhD thesis, TU Braunschweig, 2017.
2. J. D. Vann and B. Ge, "Tensor Representation of Electric Machine Windings and its Connection with Winding Functions," in IEEE ECCE 2024, Phoenix, AZ, 2024.
3. C. Ciriani, H. A. Khan, et al., "A General Approach to the Design of Multi-Layer Fractional-Slot Concentrated Windings With Arbitrary Number of Slots, Poles, and Phases," IEEE Access, vol. 12, 2024.
4. F. Scuiller, "General, compact and easy-to-compute winding factor formulation," IET Electric Power Applications, vol. 14(8), pp. 1430–1437, 2020.
5. F. N. U. Nishanth, A. Khamitov, and E. L. Severson, "Design of Electric Machine Windings to Independently Control Multiple Airgap Harmonics," IEEE Trans. Industry Applications, 2023.
6. M. Khai et al., "Algorithmic Design of Modular Two-Layer Multiphase Windings Based on Number Theory," Energies, vol. 18(23), 6320, 2025.
7. P. Bonneel, J. Le Besnerais, et al., "Pyleecan: An Open-Source Python Object-Oriented Software for the Multiphysic Design Optimization of Electrical Machines," ICEM 2018.
8. A. Selema, M. N. Ibrahim, and P. Sergeant, "Electrical Machines Winding Technology: Latest Advancements for Transportation Electrification," Machines, vol. 10(7), 563, 2022.
