"""
winding_plot - Visualization tools for winding topology.

This package provides plotting functions for:
- Winding factor harmonic spectra (star of slots, bar charts)
- MMF distributions (star of MMFs)
- Connection matrices
- Stator cross-sections with conductor placement

Author: Mang Cai (original CaisModule4Draw.py, 2016)
Refactored: 2026
"""

from winding_plot.spectrum import (
    show_winding_spectrum,
    draw_star_of_spectrums,
    draw_polar_coordinate_system,
)

from winding_plot.mmf import (
    draw_star_of_mmfs,
    draw_star_of_mmf_and_currents,
)

from winding_plot.connection import (
    draw_connection_matrix,
    draw_conductor_plan_of_connection_matrix,
    draw_conductor_plan_of_coil_group,
    draw_connection,
    draw_number_of_turn,
)

from winding_plot.stator import (
    draw_stator2,
    go_conductor,
    return_conductor,
    rotation,
)

from winding_plot.utils import (
    draw_arc_arrow,
    draw_pole_color,
    draw_phase_color,
    draw_phase_index,
    draw_pole_index,
)

__version__ = '1.0.0'
