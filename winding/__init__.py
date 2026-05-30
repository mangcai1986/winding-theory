"""
winding - Unified method for analysis and design of electrical machine winding topologies.

This package implements the unified method for winding topology treatment
introduced in Mang Cai's PhD thesis "Contribution to the Winding Theory"
(TU Braunschweig, 2017).

Modules
-------
models      : Data classes for winding topology representation.
analysis    : Winding factor harmonic spectrum and MMF analysis.
design      : Step-by-step winding topology design pipeline.
modification: Derivation of realizable winding topologies.
transforms  : Rotation and mirror symmetry detection.
utils       : Utility functions.

Examples
--------
>>> from winding.models import CurrentSystem, WindingSpectrum
>>> from winding.analysis import get_mmf
>>> from winding.design import get_primitive_multiphase_winding
"""

from winding.models import (
    WindingSpectrum, CurrentSystem, MMF,
    MultiPhaseWinding, SinglePhaseWinding, CoilGroup, Coil,
    CategoryOfCoil, ModifiedMultiPhaseWinding, PriMultiLayerTurnPitchTopo,
)

from winding.analysis import (
    winding_topology_to_spectrum,
    winding_topology_to_spectrum_with_harmonics,
    get_ideal_winding_spectrum,
    get_mmf,
    get_normalized_mmf_vector,
)

from winding.design import (
    get_primitive_multiphase_winding,
    get_single_phase_winding,
    get_coil_group,
    get_coil,
    get_property_of_coil,
)

from winding.modification import (
    winding_topology_double_way_connection,
    winding_topology_single_way_connection_md,
    winding_topology_single_way_connection_sp,
    obtain_multi_turn_winding_topology,
    obtain_multi_layer_winding_topology,
    obtain_double_layer_winding_topology,
    obtain_single_layer_winding_topology,
    obtain_set_of_connection,
    obtain_mcoil_connection,
    obtain_mcond_connection,
)

from winding.transforms import (
    detect_rotation_symmetry,
    detect_mirror_symmetry,
    get_part_of_mirror_symmetry,
    connection_vector_to_connection_matrix,
)

from winding.utils import (
    proj, calc_connection, coil_pitch,
    calculate_number_of_turns,
)

__version__ = '1.0.0'
__author__ = 'Mang Cai'
__email__ = ''
__license__ = 'MIT'
