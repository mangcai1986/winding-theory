"""
Example 4: 24-slot, 6-phase winding with 5th over-harmonic (γ = 5).

Based on thesis Chapter 6, Section 6.3.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import matplotlib
matplotlib.rcParams['text.usetex'] = False

from winding.models import CurrentSystem, WindingSpectrum
from winding.analysis import get_mmf
from winding.design import (
    get_primitive_multiphase_winding,
    get_single_phase_winding,
    get_coil_group,
    get_coil,
)

# ======================================================================
# Design Parameters
# ======================================================================
n_slots = 24
n_phases = 6
working_harmonic = 5

show_figures = True
output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
os.makedirs(output_dir, exist_ok=True)

# ======================================================================
# 1. Symmetrical Multi-Phase Current System
# ======================================================================
current_system = CurrentSystem(n_phases, current_system_flag=0)
print(f"Current system: {n_phases} phases")

# ======================================================================
# 2. Ideal Winding Spectrum
# ======================================================================
ideal_spectrum = WindingSpectrum(n_slots, working_harmonic)

# ======================================================================
# 3. Ideal MMF Distribution
# ======================================================================
ideal_mmf = get_mmf(ideal_spectrum)

# ======================================================================
# 4. Primitive Multi-Phase Winding
# ======================================================================
windings = get_primitive_multiphase_winding(ideal_mmf, current_system)
print(f"Generated {len(windings)} primitive multi-phase winding types")

# ======================================================================
# 5. Single-Phase Winding (Rotation Symmetry)
# ======================================================================
single_phase = get_single_phase_winding(windings, current_system_flag=0)
print(f"Generated {len(single_phase)} single-phase winding types")

# ======================================================================
# 6. Coil Group (Mirror Symmetry)
# ======================================================================
coil_groups = get_coil_group(single_phase)
print(f"Generated {len(coil_groups)} coil groups")

# ======================================================================
# 7. All Possible Coils
# ======================================================================
coils = get_coil(coil_groups)
print(f"Generated coils for {len(coils)} connection matrix types")

print("\n=== 24-slot, 6-phase, 5th harmonic winding design completed successfully ===")
