"""
Data classes for winding topology representation.

These classes form the hierarchical data structure used throughout
the winding analysis and design methods. The hierarchy is:

    WindingSpectrum -> MMF -> MultiPhaseWinding -> SinglePhaseWinding
        -> CoilGroup -> Coil -> PriMultiLayerTurnPitchTopo

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import numpy as np


class WindingSpectrum:
    """Winding factor harmonic spectrum of a winding topology.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    working_harmonic : int
        The working harmonic order (gamma).
    type_ : str
        'Ideal' generates a spectrum with only the working harmonic present;
        otherwise the distribution is left uninitialized (NaN).
    """

    def __init__(self, n_slots, working_harmonic, type_='Ideal'):
        self.working_harmonic = working_harmonic
        self.n_slots = n_slots
        if type_ == 'Ideal':
            self.distribution = _get_ideal_winding_spectrum(n_slots, working_harmonic)
        else:
            self.distribution = None


class CurrentSystem:
    """Multi-phase current system (symmetrical).

    Parameters
    ----------
    n_phases : int
        Number of phases.
    type_ : str
        'Symmetric' generates a symmetrical multi-phase system.
    current_system_flag : int
        0 for source current system (default),
        1 for winding design current system.
    """

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
            self.distribution = None


class MMF:
    """Magneto-motive force distribution.

    Parameters
    ----------
    winding_spectrum : WindingSpectrum
        Parent winding spectrum object.
    """

    def __init__(self, winding_spectrum):
        self.parent_winding_spectrum = winding_spectrum
        self.transformation_matrix = None
        self.distribution = None


class MultiPhaseWinding:
    """Primitive multi-phase winding topology.

    Parameters
    ----------
    mmf : MMF
        Parent MMF object.
    current_system : ndarray
        Multi-phase current system vector.
    """

    def __init__(self, mmf, current_system):
        self.parent_mmf = mmf
        self.connection_matrix = None
        self.current_system = current_system

    @property
    def working_harmonic(self):
        """Convenience: working harmonic from the parent MMF -> spectrum chain."""
        return self.parent_mmf.parent_winding_spectrum.working_harmonic


class SinglePhaseWinding:
    """Primitive single-phase winding topology (rotation symmetry exploited).

    Parameters
    ----------
    multi_phase_winding : MultiPhaseWinding
        Parent multi-phase winding object.
    """

    def __init__(self, multi_phase_winding):
        self.parent_multi_phase_winding = multi_phase_winding
        self.rotation_symmetry_matrix = None
        self.rotation_symmetry_matrix_type_ii = None
        self.connection_vector = None
        self.has_symmetry = None

    @property
    def working_harmonic(self):
        """Convenience: working harmonic from parent chain."""
        return self.parent_multi_phase_winding.working_harmonic

    @property
    def current_system(self):
        """Convenience: current system from parent chain."""
        return self.parent_multi_phase_winding.current_system


class CoilGroup:
    """Primitive coil group (mirror symmetry exploited).

    Parameters
    ----------
    single_phase_winding : SinglePhaseWinding
        Parent single-phase winding object.
    """

    def __init__(self, single_phase_winding):
        self.parent_single_phase_winding = single_phase_winding
        self.mirror_symmetry_matrix = None
        self.connection_vector = None
        self.position_of_symmetry_axis = None
        self.has_symmetry = None
        # Internal: full mirror symmetry matrix (not reduced)
        self._mirror_symmetry_matrix = None

    @property
    def working_harmonic(self):
        """Convenience: working harmonic from parent chain."""
        return self.parent_single_phase_winding.working_harmonic

    @property
    def current_system(self):
        """Convenience: current system from parent chain."""
        return self.parent_single_phase_winding.current_system

    @property
    def rotation_symmetry_matrix(self):
        """Convenience: rotation symmetry matrix from parent chain."""
        return self.parent_single_phase_winding.rotation_symmetry_matrix

    @property
    def rotation_symmetry_matrix_type_ii(self):
        """Convenience: type II rotation symmetry matrix from parent chain."""
        return self.parent_single_phase_winding.rotation_symmetry_matrix_type_ii


class Coil:
    """A single coil within a coil group.

    Parameters
    ----------
    coil_group : CoilGroup
        Parent coil group object.
    """

    def __init__(self, coil_group):
        self.parent_coil_group = coil_group
        self.connection_vector = None
        self.pitch = None
        self.position = None
        self.winding_spectrum = None
        self.connection_matrix = None


class CategoryOfCoil:
    """Category of coils grouped by pitch or spectrum.

    Parameters
    ----------
    set_of_coil : list of Coil
        Coils belonging to this category.
    """

    def __init__(self, set_of_coil):
        self.set_of_coil = set_of_coil
        self.coil_pitch = None
        self.winding_spectrum = None
        self.type_ = None  # 0 for same pitch, 1 for same spectrum


class ModifiedMultiPhaseWinding:
    """Modified (realizable) multi-phase winding topology.

    Container for all derived winding topology variants
    (multi-turn, multi-layer, multi-coil, multi-conductor, etc.).
    """

    def __init__(self):
        self.n_layers = None
        self.n_total_conductors = None
        self.multi_coil = None
        self.multi_turn = None
        self.multi_conductor = None
        self.classical = None
        self.set_of_coil = None
        self.mirror_symmetry_matrix = None
        self.rotation_symmetry_matrix = None
        self.rotation_symmetry_matrix_type_ii = None
        self.current_system = None
        self.error = None
        self.winding_spectrum = None


class PriMultiLayerTurnPitchTopo:
    """Primitive multi-layer, multi-turn winding topology (intermediate result).

    This class captures both the ideal and realized conductor distributions,
    along with the derived winding spectrum. It is the output of all
    modification pipeline functions.

    Parameters
    ----------
    conductor_distribution_ideal : ndarray
        Ideal (target) conductor distribution.
    conductor_distribution_real : ndarray
        Realized conductor distribution.
    connection_vector : ndarray
        Coil connection vector (positive/negative conductor indices).
    coil_pitch : ndarray
        Pitch of each coil.
    connection_matrix : ndarray
        Connection matrix of shape (n_slots, n_coils).
    n_turns : ndarray
        Number of turns per coil.
    error_rel : float
        Relative error of the turn approximation.
    multi_cond_matrix : ndarray
        Multi-conductor matrix (for single-way SP connections).
    msym_matrix : ndarray
        Mirror symmetry matrix (reduced, upper part).
    rsym_matrix_i : ndarray
        Rotation symmetry matrix (type I).
    rsym_matrix_ii : ndarray
        Rotation symmetry matrix (type II).
    m_pha_curr_sys : ndarray
        Multi-phase current system.
    _msym_matrix : ndarray
        Full mirror symmetry matrix (not reduced).
    working_harmonic : int
        Working harmonic order.
    """

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
        """Select a subset of coils by index.

        Parameters
        ----------
        index_of_coils : list of int
            Indices of coils to select.

        Returns
        -------
        list
            Empty list (placeholder for future implementation).
        """
        return []


# ============================================================================
# Internal helpers (avoid circular imports)
# ============================================================================

def _get_ideal_winding_spectrum(n_slots, working_harmonic):
    """Generate an ideal winding spectrum: 1 at the working harmonic, 0 elsewhere."""
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
    """Generate the winding design current system (evenly spaced phasors over pi rad)."""
    return np.exp(1j * np.linspace(0, np.pi, n_phases, endpoint=False))


def _get_current_system_of_source(current_system_4_winding_design):
    """Build the source current system by factoring out powers of two.

    The algorithm repeatedly divides the number of phases by 2.
    If an odd factor remains, the current system includes a
    zero-sequence component, and the corresponding phase indices
    are negated.

    Returns
    -------
    clamp_matrix : ndarray
        Diagonal matrix with -1 at negated phase indices.
    current_system_of_source : ndarray
        Adjusted current system vector.
    """
    m = current_system_4_winding_design.size
    current_system_of_source = np.copy(current_system_4_winding_design)
    has_zero = 0
    clamp_matrix = np.identity(m)

    m_ = m
    k = 0
    g = 0
    # Factor out powers of 2: m = 2^k * m_odd
    while True:
        if np.mod(m_, 2) == 1:
            has_zero = 1
            break
        else:
            g = 2 ** k
            k = k + 1
            m_ = m_ / 2

    if has_zero == 1:
        # Negate the phase indices corresponding to the zero-sequence component
        index = np.linspace(2 ** g, 2 * 2 ** g, 2 ** g, endpoint=False, dtype=int)
        current_system_of_source[index] = -1 * current_system_4_winding_design[index]
        clamp_matrix[index, index] = -1

    return clamp_matrix, current_system_of_source


def _s2m_cond_distri(s_cond_distri, rsym_matrix_i, rsym_matrix_ii):
    """Convert a single-phase conductor distribution to multi-phase using symmetry.

    The multi-phase distribution is reconstructed by applying successive
    rotation powers to the single-phase vector.

    Parameters
    ----------
    s_cond_distri : ndarray
        Single-phase conductor distribution.
    rsym_matrix_i : ndarray
        Rotation symmetry matrix (type I, slot rotation).
    rsym_matrix_ii : ndarray
        Rotation symmetry matrix (type II, phase rotation).

    Returns
    -------
    ndarray
        Multi-phase conductor distribution matrix.
    """
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
    """Internal: winding factor spectrum from topology (no normalization)."""
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
