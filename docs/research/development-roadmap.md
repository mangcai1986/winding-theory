# Development Roadmap

> **Last updated:** 2026-05-30
> This roadmap defines the prioritized development tasks for the winding-theory repository, driven by the research frontier analysis.

---

## Priority Overview

| Priority | Title | Target | Status |
|----------|-------|--------|--------|
| **P0** | Paper-Code Synchronization | Complete | 🔄 In Progress |
| **P1** | Academic Positioning & Comparison | 2026 Q3 | ⏳ Pending |
| **P2** | Hairpin Winding Extension | 2026 Q3 | ⏳ Pending |
| **P3** | PyLecan Integration | 2026 Q4 | ⏳ Pending |
| **P4** | Automated Winding Search | 2027 Q1 | ⏳ Pending |
| **P5** | PyPI Release & Docs | 2026 Q3 | ⏳ Pending |

---

## P0: Paper-Code Synchronization (🔄 In Progress)

**Goal:** Verify every code snippet in thesis Appendix A matches the refactored API.

**Tasks:**
- [ ] Extract Appendix A code from thesis markdown (~page 192)
- [ ] Run each code snippet with refactored API
- [ ] Verify output parameters and results
- [ ] Update [tracking.md](../thesis/tracking.md) with actual verification results
- [ ] Fix any discrepancies found

**Verification method:** Run each example end-to-end, capture output, compare with thesis figures/tables.

---

## P1: Academic Positioning & Comparison (⏳ Pending)

**Goal:** Establish the unified method's position in the current research landscape.

**Tasks:**
- [ ] Add "Related Work" section to root README
- [ ] Write a formal comparison with Vann & Ge (2024) tensor method
- [ ] Write a formal comparison with Ciriani et al. (2024) FSCW method
- [ ] Write a formal comparison with Khai et al. (2025) number theory method
- [ ] Show mathematical connection: unified method's spectrum transformation ↔ tensor C₁·C₂ product
- [ ] **Optional:** Submit a short communication to IEEE Transactions on Energy Conversion or similar

**Success criteria:** A clear, citable document showing the unified method's unique position.

---

## P2: Hairpin Winding Extension (⏳ Pending)

**Goal:** Demonstrate the unified method's applicability to hairpin (发卡) windings — the dominant EV traction motor technology.

**Tasks:**
- [ ] Create `examples/hairpin_winding.py`
- [ ] Design a 4-layer hairpin winding using `obtain_multi_layer_winding_topology`
- [ ] Validate against published hairpin winding designs (e.g., Bianchi 2018, Zou 2022)
- [ ] Create visualization of hairpin winding topology
- [ ] Compare with Vann & Ge's rank-3 tensor representation

**Success criteria:** A runnable example that produces a hairpin winding topology matching published designs.

---

## P3: PyLecan Integration (⏳ Pending)

**Goal:** Connect the unified method's design output with PyLecan's FEA simulation.

**Tasks:**
- [ ] Create `winding/export.py` module
- [ ] Implement `to_pyleecan_winding()` converter
- [ ] Create `examples/integration_pyleecan.py` showing end-to-end flow
- [ ] Document the integration in README

**Success criteria:** A winding designed by the unified method can be imported into PyLecan and simulated via FEMM.

---

## P4: Automated Winding Search (⏳ Pending)

**Goal:** Leverage the unified method's symmetry framework for automated winding topology discovery.

**Tasks:**
- [ ] Define search space: enumerate slot/pole/phase/connection combinations
- [ ] Implement automated symmetry enumeration
- [ ] Implement objective functions (maximize fundamental winding factor, minimize THD, etc.)
- [ ] Output Pareto-optimal winding topologies
- [ ] Create `examples/automated_search.py`

**Relation to Vann & Ge's future work:** They identify "exact cover problem + optimization" as future work. The unified method's symmetry-based approach is a natural fit for this.

**Success criteria:** Given N_slots, N_poles, N_phases, the system outputs the top-5 winding configurations ranked by user-specified criteria.

---

## P5: PyPI Release & Documentation (⏳ Pending)

**Goal:** `pip install winding-theory` — professional open-source package.

**Tasks:**
- [ ] Verify `pyproject.toml` is complete
- [ ] Set up Sphinx or MkDocs documentation
- [ ] Complete NumPy-style docstrings (ongoing)
- [ ] Expand unit test coverage (currently 30 tests)
- [ ] Add tests for: `normalize_cond_distri`, `s2m_cond_distri`, `sum_str_vector`, `sel`, `init_list_of_objects`
- [ ] Publish to TestPyPI → PyPI
- [ ] Set up Zenodo DOI for repository

**Success criteria:** `pip install winding-theory` works; docs hosted on GitHub Pages or ReadTheDocs.

---

## Longer-Term Vision

| Horizon | Goal |
|---------|------|
| 2026 Q4 | Repository recognized as the central hub for winding topology theory |
| 2027 | Comparison paper published; method cited by 10+ external works |
| 2027+ | Winding topology search algorithm integrated into PyLecan mainline |
| 2028 | Industry adoption: references in commercial motor design tools |

---

## How to Update This Roadmap

- When a priority is completed, change its status to ✅
- When new research reveals new opportunities, add tasks to the relevant priority
- Review and update quarterly alongside literature searches
