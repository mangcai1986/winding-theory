# Paper Reference

This document maps the code in this repository to the corresponding
sections of Mang Cai's PhD thesis.

## Thesis Information

- **Title:** Contribution to the winding theory: Introduction of a unified method for the treatment of winding topology
- **Author:** Mang Cai
- **University:** Technische Universität Braunschweig
- **Submission:** 23.11.2016
- **Defense:** 14.02.2017
- **Print Year:** 2017
- **Supervisor:** Prof. Dr.-Ing. W.-R. Canders
- **Second Reviewer:** Prof. Dr.-Ing. habil. Dr. h. c. K. Hameyer

## Code ↔ Thesis Mapping

### Chapter 5: The Proposed Method

| Code Module | Thesis Section | Description |
|-------------|---------------|-------------|
| `winding/models.py` | §5.1, §5.2 | Data classes for winding representation |
| `winding/analysis.py` | §5.3.1 | Winding factor harmonic spectrum calculation |
| `winding/transforms.py` | §5.3.2 | Rotation and mirror symmetry detection |
| `winding/design.py` | §5.3.3–§5.3.6 | Design pipeline: MMF → coils |
| `winding/modification.py` | §5.3.7 | Double-way, single-way connections |

### Appendix A: Python Implementation

| Thesis Code | Repository Function |
|-------------|-------------------|
| `WindingSchema2WindingSpectrum` | `winding.analysis.winding_topology_to_spectrum` |
| `DrawStarOfSpectrums` | `winding_plot.spectrum.draw_star_of_spectrums` |
| `DrawStarOfMMFs` | `winding_plot.mmf.draw_star_of_mmfs` |
| `DrawConnectionMatrix` | `winding_plot.connection.draw_connection_matrix` |
| `DrawConductorPlanOfConnectionMatrix` | `winding_plot.connection.draw_conductor_plan_of_connection_matrix` |
| `GetMMF` | `winding.analysis.get_mmf` |
| `GetPrimitiveMultiPhaseWinding` | `winding.design.get_primitive_multiphase_winding` |
| `GetSinglePhaseWinding` | `winding.design.get_single_phase_winding` |
| `GetCoilGroup` | `winding.design.get_coil_group` |
| `WindingTopologyDoubleWayConnection` | `winding.modification.winding_topology_double_way_connection` |
| `WindingTopologySingleWayConnectionMD` | `winding.modification.winding_topology_single_way_connection_md` |
| `WindingTopologySingleWayConnectionSP` | `winding.modification.winding_topology_single_way_connection_sp` |
| `ObtainMultiTurnWindingTopology` | `winding.modification.obtain_multi_turn_winding_topology` |
| `ObtainMultiLayerWindingTopology` | `winding.modification.obtain_multi_layer_winding_topology` |
| `ObtainDoubleLayerWindingTopology2` | `winding.modification.obtain_double_layer_winding_topology` |
| `ObtainSingleLayerWindingTopology2` | `winding.modification.obtain_single_layer_winding_topology` |

### Chapter 6: Application Examples

| Thesis Section | Example Script |
|---------------|---------------|
| §6.1: 12 slots, 3 phases, γ=1 and γ=5 | `examples/01_fundamental_harmonic.py`, `examples/02_over_harmonic.py` |
| §6.2: 9 slots, 3 phases, γ=4 | `examples/03_9_slot_4_harmonic.py` |
| §6.3: 24 slots, 6 phases, γ=5 | `examples/04_24_slot_6_phase.py` |
