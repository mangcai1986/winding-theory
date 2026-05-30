"""
Example 4 (Full): 24-slot, 6-phase winding with 5th over-harmonic (γ = 5).

Based on thesis Chapter 6, Section 6.3.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['text.usetex'] = False
import matplotlib.pyplot as plt
import numpy as np

from winding.models import CurrentSystem, WindingSpectrum
from winding.analysis import get_mmf
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
from winding_plot.spectrum import show_winding_spectrum

N_SLOTS = 24; N_PHASES = 6; WORKING_HARMONIC = 5
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output', 'ex04')
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 60)
print("Example 4: 24-slot, 6-phase, 5th over-harmonic (γ=5)")
print("=" * 60)

current_system = CurrentSystem(N_PHASES, current_system_flag=0)
print(f"Current system: {N_PHASES} phases")

ideal_mmf = get_mmf(WindingSpectrum(N_SLOTS, WORKING_HARMONIC))

windings = get_primitive_multiphase_winding(ideal_mmf, current_system)
sp = get_single_phase_winding(windings, 0)
cg = get_coil_group(sp)
coils = get_coil(cg)

dw = winding_topology_double_way_connection(cg)
sw_md = winding_topology_single_way_connection_md(cg)
sw_sp = winding_topology_single_way_connection_sp(cg)
mt = obtain_multi_turn_winding_topology(dw)
ml = obtain_multi_layer_winding_topology(mt)
dl = obtain_double_layer_winding_topology(sw_md)
sl = obtain_single_layer_winding_topology(mt)

print(f"Primitive windings: {len(windings)} types")
print(f"Coil groups: {len(cg)} groups")
for i, c in enumerate(coils): print(f"  Coils type {i+1}: {len(c)}")
print(f"Double-way: {len(dw)}, Multi-coil: {len(sw_md)}, Multi-conductor: {len(sw_sp)}")
print(f"Multi-turn: {len(mt)}, Multi-layer: {len(ml)}")
print(f"Double-layer: {len(dl)}, Single-layer: {len(sl)}")

print("\n--- Winding Factor Comparison ---")
for label, topologies in [("Double-layer", dl), ("Single-layer", sl)]:
    for i, topo in enumerate(topologies):
        ws = topo.winding_spectrum_real
        idx = N_SLOTS // 2 + WORKING_HARMONIC - 1
        wf = np.abs(ws[idx])
        print(f"  {label} type {i+1}: |ξ({WORKING_HARMONIC})| = {wf:.4f}")

if dl:
    fig = plt.figure(facecolor='w', figsize=(6, 4), dpi=100)
    show_winding_spectrum(dl[0].winding_spectrum_real)
    fig.savefig(os.path.join(OUTPUT_DIR, 'double_layer_spectrum.pdf')); plt.close(fig)

print(f"\nFigures saved to: {OUTPUT_DIR}")
print("=== Example 4 completed successfully ===")
