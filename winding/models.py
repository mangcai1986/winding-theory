"""
Data classes for winding topology representation.

These classes form the hierarchical data structure used throughout
the winding analysis and design methods. The hierarchy is:

    WindingSpectrum → MMF → MultiPhaseWinding → SinglePhaseWinding
        → CoilGroup → Coil → PriMultiLayerTurnPitchTopo

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import numpy as np


class WindingSpectrum:
    """Winding factor harmonic spectrum of a winding topology."""

    def __init__(self, n_slots, working_harmonic, type_='Ideal'):
        self.working_harmonic = working_harmonic
        self.n_slots = n_slots
        if type_ == 'Ideal':
            self.distribution = _get_ideal_winding_spectrum(n_slots, working_harmonic)
        else:
            self.distribution = np.nan


class CurrentSystem:
    """Multi-phase current system (symmetrical)."""

    def __init__(self, n_phases, type_='Symmetric', current_system_flag=0):
        self.n_phases = n_phases
        self.current_system_flag = current_system_flag
        if type_ == 'Symmetric':
            self.distribution_4_winding_design = _get_current_system_4_winding_design(n_phases)
            self.clamp_matrix, self.distribution_of_source = _get_current_system_of_source(
                self.distribution_4_winding_design)
            if current_system_flag == 0:
                self.distribution = self.distribution_of_source
            elif current_system_flag == 1:
                self.distribution = self.distribution_4_winding_design
        else:
            self.distribution = np.nan


class MMF:
    """Magneto-motive force distribution."""

    def __init__(self, winding_spectrum):
        self.parent_winding_spectrum = winding_spectrum
        self.transformation_matrix = np.nan
        self.distribution = np.nan


class MultiPhaseWinding:
    """Primitive multi-phase winding topology."""

    def __init__(self, mmf, current_system):
        self.parent_mmf = mmf
        self.connection_matrix = np.nan
        self.current_system = current_system


class SinglePhaseWinding:
    """Primitive single-phase winding topology."""

    def __init__(self, multi_phase_winding):
        self.parent_multi_phase_winding = multi_phase_winding
        self.rotation_symmetry_matrix = np.nan
        self.rotation_symmetry_matrix_type_ii = np.nan
        self.connection_vector = np.nan
        self.has_symmetry = np.nan


class CoilGroup:
    """Primitive coil group (mirror symmetry exploited)."""

    def __init__(self, single_phase_winding):
        self.parent_single_phase_winding = single_phase_winding
        self.mirror_symmetry_matrix = np.nan
        self.connection_vector = np.nan
        self.position_of_symmetry_axis = np.nan
        self.has_symmetry = np.nan


class Coil:
    """A single coil within a coil group."""

    def __init__(self, coil_group):
        self.parent_coil_group = coil_group
        self.connection_vector = np.nan
        self.pitch = np.nan
        self.position = np.nan
        self.winding_spectrum = np.nan
        self.connection_matrix = np.nan


class CategoryOfCoil:
    """Category of coils grouped by pitch or spectrum."""

    def __init__(self, set_of_coil):
        self.set_of_coil = set_of_coil
        self.coil_pitch = np.nan
        self.winding_spectrum = np.nan
        self.type_ = np.nan  # 0 for same pitch, 1 for same spectrum


class ModifiedMultiPhaseWinding:
    """Modified (realizable) multi-phase winding topology."""

    def __init__(self):
        self.n_layers = np.nan
        self.n_total_conductors = np.nan
        self.multi_coil = np.nan
        self.multi_turn = np.nan
        self.multi_conductor = np.nan
        self.classical = np.nan
        self.set_of_coil = np.nan
        self.mirror_symmetry_matrix = np.nan
        self.rotation_symmetry_matrix = np.nan
        self.rotation_symmetry_matrix_type_ii = np.nan
        self.current_system = np.nan
        self.error = np.nan
        self.winding_spectrum = np.nan


class PriMultiLayerTurnPitchTopo:
    """Primitive multi-layer, multi-turn winding topology (intermediate result)."""

    def __init__(self, conductor_distribution_ideal, conductor_distribution_real,
                 connection_vector, coil_pitch, connection_matrix, n_turns, error_rel,
                 multi_cond_matrix=0, msym_matrix=0, rsym_matrix_i=0, rsym_matrix_ii=0,
                 m_pha_curr_sys=0, _msym_matrix=0, working_harmonic=0):
        self.working_harmonic = working_harmonic
        self.conductor_distribution_ideal = conductor_distribution_ideal
        self.cond_distri_ideal_part_ii = _msym_matrix.dot(conductor_distribution_ideal)
        self.conductor_distribution_real = conductor_distribution_real
        self.connection_vector = connection_vector
        self.coil_pitch = coil_pitch
        self.connection_matrix = connection_matrix
        self.connection_matrix_part_ii = _msym_matrix.dot(self.connection_matrix)
        self.n_turns = n_turns
        self.error_rel = error_rel
        self.multi_cond_matrix = multi_cond_matrix
        self.set_of_coil = connection_matrix[:, :] * n_turns[:] + multi_cond_matrix
        self.set_of_coil_part_ii = _msym_matrix.dot(self.set_of_coil)
        self.n_coils = np.size(n_turns)
        self.m_pha_curr_sys = m_pha_curr_sys
        self.msym_matrix = msym_matrix
        self._msym_matrix = _msym_matrix
        self.rsym_matrix_i = rsym_matrix_i
        self.rsym_matrix_ii = rsym_matrix_ii

        # Real winding topology and spectrum
        self.s_cond_distri_real = self.msym_matrix.dot(self.conductor_distribution_real)
        self.m_cond_distri_real = _s2m_cond_distri(self.s_cond_distri_real, self.rsym_matrix_i, self.rsym_matrix_ii)
        self.winding_spectrum_real = _winding_topology_to_spectrum(self.m_cond_distri_real, self.m_pha_curr_sys)

        # Ideal winding topology and spectrum
        self.s_cond_distri_ideal = self.msym_matrix.dot(self.conductor_distribution_ideal)
        self.m_cond_distri_ideal = _s2m_cond_distri(self.s_cond_distri_ideal, self.rsym_matrix_i, self.rsym_matrix_ii)
        self.winding_spectrum_ideal = _winding_topology_to_spectrum(self.m_cond_distri_ideal, self.m_pha_curr_sys)

    def select_coils(self, index_of_coils):
        return []


# ============================================================================
# Internal helpers (avoid circular imports)
# ============================================================================

def _get_ideal_winding_spectrum(n_slots, working_harmonic):
    if bool(n_slots % 2):
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2
    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots, dtype=int)

    ideal_spectrum = np.zeros(n_slots)
    ideal_spectrum[harmonic_vector == working_harmonic] = 1
    return ideal_spectrum


def _get_current_system_4_winding_design(n_phases):
    return np.exp(1j * np.linspace(0, np.pi, n_phases, endpoint=False))


def _get_current_system_of_source(current_system_4_winding_design):
    m = current_system_4_winding_design.size
    current_system_of_source = np.copy(current_system_4_winding_design)
    has_zero = 0
    clamp_matrix = np.identity(m)

    m_ = m
    k = 0
    g = 0
    while True:
        if np.mod(m_, 2) == 1:
            has_zero = 1
            break
        else:
            g = 2 ** k
            k = k + 1
            m_ = m / 2

    if has_zero == 1:
        index = np.linspace(2 ** g, 2 * 2 ** g, 2 ** g, endpoint=False, dtype=int)
        current_system_of_source[index] = -1 * current_system_4_winding_design[index]
        clamp_matrix[index, index] = -1

    return clamp_matrix, current_system_of_source


def _s2m_cond_distri(s_cond_distri, rsym_matrix_i, rsym_matrix_ii):
    from numpy import linalg as LA
    n_phases = np.size(rsym_matrix_ii, axis=0)
    n_slots = np.size(rsym_matrix_i, axis=0)
    connection_matrix_of_coil_ = np.zeros((n_slots, n_phases))
    connection_matrix_of_coil_[:, 0] = s_cond_distri
    m_cond_distri = connection_matrix_of_coil_
    for k in range(1, n_phases):
        m_cond_distri = m_cond_distri + LA.matrix_power(rsym_matrix_i, k).dot(connection_matrix_of_coil_).dot(
            LA.matrix_power(rsym_matrix_ii, k))
    return m_cond_distri


def _winding_topology_to_spectrum(winding_topology, current_phase_vector):
    n_slots = np.size(winding_topology, axis=0)
    position_vector = np.linspace(1, n_slots, n_slots)

    if bool(n_slots % 2):
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2
    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots)

    position_matrix, harmonic_matrix = np.meshgrid(position_vector, harmonic_vector)
    transformation_matrix = np.exp(-1j * harmonic_matrix * 2 * np.pi / n_slots * position_matrix)

    winding_topology_norm = winding_topology / np.sum(np.abs(winding_topology))
    return transformation_matrix.dot(winding_topology_norm.dot(current_phase_vector))
