# Contribution to the Winding Theory

A unified method for the analysis and design of electrical machine winding topologies.

This repository contains the Python implementation of the unified winding topology
treatment method introduced in **Mang Cai's PhD thesis** (TU Braunschweig, 2017):

> **Contribution to the winding theory: Introduction of a unified method for the treatment of winding topology**

## About

The winding of an electrical machine is the key component of the electromechanical
energy conversion process. This work introduces a unified, deterministic method for
the analysis and design of winding topologies that can handle all conventional
winding types:

- Double-layer windings
- Single-layer windings
- Multi-layer windings
- Multi-turn windings
- Multi-coil windings
- Multi-conductor windings
- Over-harmonic windings

The method is described using four complementary "languages":
1. **Mathematical formulation** via matrix notation
2. **Graphical presentation** via novel illustrations
3. **Python implementation** (this repository)
4. **Natural language** in the thesis itself

## Installation

```bash
# Clone the repository
git clone https://github.com/mangcai/winding-theory.git
cd winding-theory

# Install dependencies
pip install numpy matplotlib

# Install the package (optional)
pip install -e .
```

## Quick Start

```python
import numpy as np
from winding.models import CurrentSystem, WindingSpectrum
from winding.analysis import get_mmf
from winding.design import (
    get_primitive_multiphase_winding,
    get_single_phase_winding,
    get_coil_group,
    get_coil,
)

# Design a 12-slot, 3-phase winding with fundamental harmonic
n_slots = 12
n_phases = 3
working_harmonic = 1

# 1. Ideal winding spectrum
ideal_spectrum = WindingSpectrum(n_slots, working_harmonic)

# 2. Ideal MMF distribution
ideal_mmf = get_mmf(ideal_spectrum)

# 3. Symmetrical multi-phase current system
current_system = CurrentSystem(n_phases, current_system_flag=0)

# 4. Primitive multi-phase winding
windings = get_primitive_multiphase_winding(ideal_mmf, current_system)

# 5. Single-phase winding (rotation symmetry)
single_phase = get_single_phase_winding(windings, current_system_flag=0)

# 6. Coil group (mirror symmetry)
coil_groups = get_coil_group(single_phase)

# 7. All possible coils
coils = get_coil(coil_groups)
```

## Examples

Run the example scripts to see the winding design pipeline in action:

```bash
python examples/01_fundamental_harmonic.py
python examples/02_over_harmonic.py
python examples/03_9_slot_4_harmonic.py
python examples/04_24_slot_6_phase.py
```

## Repository Structure

```
winding-theory/
├── winding/           # Core Python package
│   ├── models.py      # Data classes
│   ├── analysis.py    # Winding spectrum and MMF analysis
│   ├── design.py      # Winding topology design
│   ├── modification.py# Derivation of realizable topologies
│   ├── transforms.py  # Symmetry detection
│   └── utils.py       # Utility functions
├── winding_plot/      # Visualization package
├── examples/          # Runable example scripts
├── tests/             # Unit tests
└── docs/              # Documentation
    ├── paper_reference.md   # Code ↔ Thesis mapping
    ├── thesis/              # Original thesis files
    └── research/            # Research tracking & literature survey
```

## Research & Frontier Tracking

This repository maintains a **living literature survey** and **development roadmap**
to track the state of the art in winding topology theory:

- [Literature Survey](docs/research/literature-survey.md) — Categorized survey of all related work since 2016
- [Method Comparison](docs/research/comparison-with-unified-method.md) — How the unified method compares to tensor, FSCW, and other approaches
- [Frontier Tracking Log](docs/research/frontier-tracking-log.md) — Timestamped search records, continuously updated
- [Citation Tracking](docs/research/citation-tracking.md) — Who cites the thesis and how
- [Development Roadmap](docs/research/development-roadmap.md) — P0–P5 prioritized implementation plan

**Goal:** Make this repository the world's central hub for winding topology theory.

## Citation

If you use this work in academic research, please cite:

```bibtex
@phdthesis{cai2017winding,
  author  = {Mang Cai},
  title   = {Contribution to the winding theory: Introduction of a unified
             method for the treatment of winding topology},
  school  = {Technische Universit\"at Braunschweig},
  year    = {2017},
  note    = {Druckjahr: 2017}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.

Copyright (c) 2017 Mang Cai
