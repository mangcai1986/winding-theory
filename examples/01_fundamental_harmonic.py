"""
Example 1: 12-slot, 3-phase winding with fundamental harmonic (γ = 1).

This demonstrates the complete design pipeline from ideal winding spectrum
to primitive multi-phase winding, single-phase winding, coil group, and coils.

Based on thesis Chapter 6, Section 6.1.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import matplotlib
matplotlib.rcParams['text.usetex'] = False

import matplotlib.pyplot as plt
import numpy as np
from winding.models import CurrentSystem, WindingSpectrum
from winding.analysis import get_mmf, winding_topology_to_spectrum
from winding.design import (
    get_primitive_multiphase_winding,
    get_single_phase_winding,
    get_coil_group,
    get_coil,
)

# ======================================================================
# Design Parameters
# ======================================================================
n_slots = 12
n_phases = 3
working_harmonic = 1

# Phase colors for visualization
phase_colors = ['lime', 'gold', 'cyan', 'green', 'r', 'b']
phase_current_colors = ['b', 'b', 'b', 'b', 'b', 'b']

show_figures = True
output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
os.makedirs(output_dir, exist_ok=True)

# ======================================================================
# 1. Symmetrical Multi-Phase Current System
# ======================================================================
current_system = CurrentSystem(n_phases, current_system_flag=0)

if show_figures:
    plt.figure(facecolor='w', figsize=(4, 4), dpi=100)
    from winding_plot.mmf import draw_star_of_mmfs
    draw_star_of_mmfs(current_system.distribution, 'b')
    plt.savefig(os.path.join(output_dir, '601_1_current_system.pdf'))

# ======================================================================
# 2. Ideal Winding Spectrum
# ======================================================================
ideal_spectrum = WindingSpectrum(n_slots, working_harmonic)

if show_figures:
    plt.figure(facecolor='white', figsize=(4, 4), dpi=100)
    from winding_plot.spectrum import draw_star_of_spectrums
    draw_star_of_spectrums(ideal_spectrum.distribution, 'r')
    plt.savefig(os.path.join(output_dir, '602_1_ideal_spectrum.pdf'))

# ======================================================================
# 3. Ideal MMF Distribution
# ======================================================================
ideal_mmf = get_mmf(ideal_spectrum)

if show_figures:
    plt.figure(facecolor='w', figsize=(4, 4), dpi=100)
    draw_star_of_mmfs(ideal_mmf.distribution, 'r')
    plt.savefig(os.path.join(output_dir, '603_1_ideal_mmf.pdf'))

# ======================================================================
# 4. Primitive Multi-Phase Winding
# ======================================================================
windings = get_primitive_multiphase_winding(ideal_mmf, current_system)

print(f"Generated {len(windings)} primitive multi-phase winding types")
for i, w in enumerate(windings):
    print(f"  Type {i+1}: connection matrix shape = {w.connection_matrix.shape}")

# ======================================================================
# 5. Single-Phase Winding (Rotation Symmetry)
# ======================================================================
single_phase = get_single_phase_winding(windings, current_system_flag=0)
print(f"\nGenerated {len(single_phase)} single-phase winding types")

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

print("\n=== Design pipeline completed successfully ===")
