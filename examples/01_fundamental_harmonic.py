"""
Example 1 (Full): 12-slot, 3-phase winding with fundamental harmonic (γ = 1).

Complete end-to-end demonstration: from ideal winding spectrum through
the full design pipeline to realizable winding topologies (multi-turn,
multi-layer, double-layer, single-layer, multi-coil, multi-conductor).

Based on thesis Chapter 6, Section 6.1.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['text.usetex'] = False
import matplotlib.pyplot as plt
import numpy as np

from winding.models import CurrentSystem, WindingSpectrum
from winding.analysis import get_mmf, winding_topology_to_spectrum
from winding.design import (
    get_primitive_multiphase_winding, get_single_phase_winding,
    get_coil_group, get_coil,
)
from winding.modification import (
    winding_topology_double_way_connection,
    winding_topology_single_way_connection_md,
    winding_topology_single_way_connection_sp,
    obtain_multi_turn_winding_topology,
    obtain_multi_layer_winding_topology,
    obtain_double_layer_winding_topology,
    obtain_single_layer_winding_topology,
)

from winding_plot.spectrum import draw_star_of_spectrums
from winding_plot.mmf import draw_star_of_mmfs
from winding_plot.connection import draw_conductor_plan_of_connection_matrix
from winding_plot.stator import draw_stator2

# ======================================================================
# Design Parameters
# ======================================================================
N_SLOTS = 12
N_PHASES = 3
WORKING_HARMONIC = 1
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output', 'ex01')
os.makedirs(OUTPUT_DIR, exist_ok=True)

PHASE_COLORS = ['lime', 'gold', 'cyan', 'green', 'r', 'b']

print("=" * 60)
print("Example 1: 12-slot, 3-phase, fundamental harmonic (γ=1)")
print("=" * 60)

# ======================================================================
# 1. Current System
# ======================================================================
print("\n[1/8] Symmetrical multi-phase current system ...")
current_system = CurrentSystem(N_PHASES, current_system_flag=0)

fig = plt.figure(facecolor='w', figsize=(4, 4), dpi=100)
draw_star_of_mmfs(current_system.distribution, 'b')
fig.savefig(os.path.join(OUTPUT_DIR, '01_current_system.pdf'))
plt.close(fig)

# ======================================================================
# 2. Ideal Winding Spectrum
# ======================================================================
print("[2/8] Ideal winding factor harmonic spectrum ...")
ideal_spectrum = WindingSpectrum(N_SLOTS, WORKING_HARMONIC)

fig = plt.figure(facecolor='white', figsize=(4, 4), dpi=100)
draw_star_of_spectrums(ideal_spectrum.distribution, 'r')
fig.savefig(os.path.join(OUTPUT_DIR, '02_ideal_spectrum.pdf'))
plt.close(fig)

# ======================================================================
# 3. Ideal MMF
# ======================================================================
print("[3/8] Ideal normalized MMF distribution ...")
ideal_mmf = get_mmf(ideal_spectrum)

fig = plt.figure(facecolor='w', figsize=(4, 4), dpi=100)
draw_star_of_mmfs(ideal_mmf.distribution, 'r')
fig.savefig(os.path.join(OUTPUT_DIR, '03_ideal_mmf.pdf'))
plt.close(fig)

# ======================================================================
# 4. Primitive Multi-Phase Winding
# ======================================================================
print("[4/8] Primitive multi-phase winding ...")
windings = get_primitive_multiphase_winding(ideal_mmf, current_system)
print(f"       → {len(windings)} types")

# ======================================================================
# 5. Single-Phase Winding
# ======================================================================
print("[5/8] Single-phase winding (rotation symmetry) ...")
single_phase = get_single_phase_winding(windings, current_system_flag=0)
print(f"       → {len(single_phase)} types")

# ======================================================================
# 6. Coil Group
# ======================================================================
print("[6/8] Coil group (mirror symmetry) ...")
coil_groups = get_coil_group(single_phase)
print(f"       → {len(coil_groups)} groups")

# ======================================================================
# 7. Coils
# ======================================================================
print("[7/8] All possible coils ...")
coils = get_coil(coil_groups)
for i, c in enumerate(coils):
    print(f"       → Type {i+1}: {len(c)} coils")

# ======================================================================
# 8. Realizable Winding Topologies (Modification Pipeline)
# ======================================================================
print("[8/8] Realizable winding topologies ...")

# --- Double-Way Connection (multi-layer) ---
dw = winding_topology_double_way_connection(coil_groups)
print(f"       Double-way connection: {len(dw)} topologies")

# --- Single-Way: Minimal Deviation (multi-coil) ---
sw_md = winding_topology_single_way_connection_md(coil_groups)
print(f"       Single-way MD (multi-coil): {len(sw_md)} topologies")

# --- Single-Way: Shortest Path (multi-conductor) ---
sw_sp = winding_topology_single_way_connection_sp(coil_groups)
print(f"       Single-way SP (multi-conductor): {len(sw_sp)} topologies")

# --- Multi-Turn ---
mt = obtain_multi_turn_winding_topology(dw)
print(f"       Multi-turn: {len(mt)} topologies")

# --- Multi-Layer ---
ml = obtain_multi_layer_winding_topology(mt)
print(f"       Multi-layer: {len(ml)} topologies")

# --- Double-Layer ---
dl = obtain_double_layer_winding_topology(sw_md)
print(f"       Double-layer: {len(dl)} topologies")

# --- Single-Layer ---
sl = obtain_single_layer_winding_topology(mt)
print(f"       Single-layer: {len(sl)} topologies")

# --- Winding factor comparison ---
print("\n--- Winding Factor Comparison ---")
for i, topo in enumerate(dl):
    ws = topo.winding_spectrum_real
    wf_working = np.abs(ws[N_SLOTS // 2 + WORKING_HARMONIC - 1]) if N_SLOTS % 2 == 0 else np.abs(ws[(N_SLOTS-1)//2 + WORKING_HARMONIC])
    print(f"  Double-layer type {i+1}: |ξ({WORKING_HARMONIC})| = {wf_working:.4f}")

for i, topo in enumerate(sl):
    ws = topo.winding_spectrum_real
    wf_working = np.abs(ws[N_SLOTS // 2 + WORKING_HARMONIC - 1]) if N_SLOTS % 2 == 0 else np.abs(ws[(N_SLOTS-1)//2 + WORKING_HARMONIC])
    print(f"  Single-layer type {i+1}: |ξ({WORKING_HARMONIC})| = {wf_working:.4f}")

# --- Plot the real winding spectrum for best topology ---
fig = plt.figure(facecolor='w', figsize=(6, 4), dpi=100)
if dl:
    ws = dl[0].winding_spectrum_real
    from winding_plot.spectrum import show_winding_spectrum
    show_winding_spectrum(ws)
    fig.savefig(os.path.join(OUTPUT_DIR, '08_double_layer_spectrum.pdf'))
plt.close(fig)

print(f"\nAll figures saved to: {OUTPUT_DIR}")
print("=== Example 1 completed successfully ===")
