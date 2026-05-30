# Comparison: Related Methods vs. the Unified Method

> **Last updated:** 2026-05-30
> This document provides an in-depth technical comparison between Mang Cai's unified winding topology method and other major approaches.

---

## 1. Tensor Representation (Vann & Ge, ECCE 2024)

### Their Approach
- Represent windings using two rank-2 tensors: C₁ (coil sides to slots) and C₂ (coils to phases)
- C₁·C₂ product yields the differential of the winding function
- For hairpin windings, rank increases to 3 (adding layer dimension)
- Focus: **representation and analysis** of existing windings

### Unified Method Approach
- Start from the ideal winding factor spectrum
- Derive MMF distribution → multi-phase winding → single-phase winding (rotation symmetry) → coil group (mirror symmetry) → coils
- Focus: **design synthesis** from specifications

### Key Differences

| Aspect | Tensor Method | Unified Method |
|--------|--------------|----------------|
| **Direction** | Bottom-up (slot → tensor) | Top-down (spectrum → winding) |
| **Design capability** | No explicit design pipeline | Complete design pipeline |
| **Harmonic analysis** | Via Fourier of winding function | Direct DFT-like transformation |
| **Symmetry analysis** | Not explicitly used | Core mechanism |
| **Multi-phase** | Not demonstrated >3 phases | Arbitrary phase count |
| **Winding types** | 5 types shown | All conventional types |
| **Mathematical foundation** | Tensor algebra | Matrix representation + symmetry groups |

### Why Both Methods Matter
The tensor method's C₁·C₂ product is mathematically related to what the unified method's `winding_topology_to_spectrum()` computes. A formal mathematical connection between these two representations would be a valuable contribution.

---

## 2. General Approach to Multi-Layer FSCW (Ciriani et al., IEEE Access 2024)

### Their Approach
- Define winding vectors for multi-layer fractional-slot concentrated windings
- Handle arbitrary slot/pole/phase combinations for FSCW specifically
- Provide a step-by-step design procedure

### Key Differences

| Aspect | Ciriani et al. | Unified Method |
|--------|---------------|----------------|
| **Scope** | Multi-layer FSCW only | All winding types |
| **Winding types** | Concentrated windings | Integer slot, fractional slot, single/double/multi-layer, multi-turn, multi-coil, multi-conductor |
| **Method** | Winding vector construction | Symmetry detection + matrix operations |
| **Harmonic analysis** | Not integrated | Full harmonic spectrum |
| **Theoretical foundation** | Phase current identification | Rotation + mirror symmetry groups |

### Comparison Result
The unified method is **broader in scope** and **deeper in theoretical foundation**. Ciriani et al. provide a useful practical procedure for a narrower class of windings.

---

## 3. Winding Factor Compact Formulation (Scuiller, IET EPA 2020)

### Their Approach
- Derive algebraic expressions for winding factor without star-of-slots
- Compact formulation for distributed and pitch factors

### Key Differences

| Aspect | Scuiller | Unified Method |
|--------|----------|----------------|
| **Purpose** | Winding factor calculation | Complete winding design |
| **Mathematical form** | Closed-form algebraic | DFT-like matrix transformation |
| **Generality** | Standard winding layouts | Arbitrary connection matrices |
| **Design** | No | Yes (full pipeline) |

### Integration Potential
Scuiller's compact formulas could serve as a **fast alternative** to the DFT-like transformation for standard winding types, while the unified method's transformation handles arbitrary/non-standard configurations.

---

## 4. Number Theory Algorithmic Design (Khai et al., Energies 2025)

### Their Approach
- Use GCD and modular arithmetic to construct winding diagrams
- Algorithmic, procedural method for two-layer multiphase windings

### Key Differences

| Aspect | Khai et al. | Unified Method |
|--------|-------------|----------------|
| **Mathematical tool** | Number theory (GCD, modulo) | Symmetry groups, linear algebra |
| **Winding layers** | Two-layer only | Single, double, multi-layer |
| **Design automation** | Algorithmic | Step-by-step with symmetry |
| **Physical insight** | Limited (purely algebraic) | Deep (symmetry = physical structure) |

### Comparison Result
The number theory approach is computationally efficient but lacks the physical interpretability of the symmetry-based approach. The unified method's symmetry matrices directly correspond to physical winding structure.

---

## 5. Open-Source Tools (PyLecan, FEMM)

### PyLecan
- Full multiphysics simulation framework
- Winding definition is part of machine model, not a design tool
- **No symmetry analysis**, no harmonic spectrum from symmetry
- **Best used as validation backend** for unified method designs

### FEMM
- Standard FEA tool
- Can validate winding factor predictions
- No winding design capability

---

## Summary: What the Unified Method Offers That Others Don't

| Capability | Unified Method | Others |
|-----------|---------------|--------|
| ✅ Ideal spectrum → realizable winding | **Unique** | None |
| ✅ All winding types in one framework | **Unique** | Partial (Ciriani: FSCW only) |
| ✅ Symmetry as design principle | **Unique** | None |
| ✅ Complete analysis + design pipeline | **Unique** | Partial (Vann & Ge: analysis only) |
| ✅ Arbitrary phase count | **Unique** | Partial (Ciriani: arbitrary) |
| ✅ Harmonic spectrum via transformation | Shared | Scuiller (compact form) |
| ✅ FEA validation integration | Possible | PyLecan (built-in) |

> **Conclusion:** The unified method occupies a unique position in the winding topology landscape — no other published work combines (a) complete design synthesis from ideal harmonics, (b) symmetry-based analysis, and (c) coverage of all conventional winding types in a single framework.

---

## Future Comparison Tasks

- [ ] Formally connect the unified method's `winding_topology_to_spectrum()` with Vann & Ge's C₁·C₂ product
- [ ] Implement Ciriani et al.'s FSCW design procedure and compare outputs
- [ ] Benchmark winding factor computation speed: DFT vs. Scuiller's compact form
- [ ] Design a unified test case (e.g., 24-slot 10-pole 3-phase) across all methods
