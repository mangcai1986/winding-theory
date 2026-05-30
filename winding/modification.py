"""
Winding topology modification functions.

Functions for deriving realizable winding topologies from primitive
coil groups through various connection strategies:

- Double-way connection (multi-layer approximation)
- Single-way connection: minimal deviation (multi-coil)
- Single-way connection: shortest path (multi-conductor)
- Multi-turn, multi-layer, double-layer, and single-layer derivations

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import numpy as np
from numpy import linalg as LA
from winding.models import PriMultiLayerTurnPitchTopo
from winding.utils import coil_pitch, calculate_number_of_turns
from winding.analysis import winding_topology_to_spectrum
from winding.transforms import connection_vector_to_connection_matrix


# ============================================================================
# Constants
# ============================================================================

# Scaling factor for converting float conductor distributions to integers.
# The ideal distribution is normalized to [0,1]; multiplying by N*100 gives
# a resolution of 1/(N*100) for integer rounding.
_CONDUCTOR_INT_SCALE = 100


# ============================================================================
# Connection enumeration functions
# ============================================================================

def obtain_connection(conductor_distribution):
    """Enumerate all possible double-way connections for a conductor distribution.

    A double-way connection starts from each positive conductor and traverses
    alternatingly to the nearest negative and positive conductors, forming a
    closed path that returns to the starting point.

    Parameters
    ----------
    conductor_distribution : ndarray
        Integer conductor distribution vector.

    Returns
    -------
    list of list
        Each element is a list of slot indices forming a connection path.
    """
    N = conductor_distribution.size
    idx_p_ = np.where(conductor_distribution > 0)[0].astype(float)
    idx_n_ = np.where(conductor_distribution < 0)[0].astype(float)

    possible_connections = []
    for i in range(idx_p_.size):
        connection = []
        idx_p = idx_p_.copy()
        idx_n = idx_n_.copy()

        idx_p0 = idx_p[i]
        connection.append(idx_p0)
        idx_p = idx_p[np.where(np.logical_not(idx_p0 == idx_p))]
        idx_p_current = idx_p0

        while True:
            idx_n_current = idx_n[np.argmin(coil_pitch(idx_n, idx_p_current, N))]
            connection.append(idx_n_current)
            idx_n = idx_n[np.where(np.logical_not(idx_n_current == idx_n))]

            if idx_p.size == 0 and idx_n.size == 0:
                break

            idx_p_current = idx_p[np.argmin(coil_pitch(idx_p, idx_n_current, N))]
            connection.append(idx_p_current)
            idx_p = idx_p[np.where(np.logical_not(idx_p_current == idx_p))]

            if idx_p.size == 0 and idx_n.size == 0:
                break

        if len(connection) % 2 == 0:
            connection.append(idx_p0)
        possible_connections.append(connection)

    return possible_connections


def obtain_set_of_connection(conductor_distribution):
    """Obtain the optimal set of connections (minimizing total path + unique pitches).

    Parameters
    ----------
    conductor_distribution : ndarray
        Integer conductor distribution vector.

    Returns
    -------
    set_of_connection : ndarray
        Array of shape (n_coils, 2) with [positive, negative] conductor indices.
    set_of_coil_pitch : ndarray
        Coil pitch for each connection.
    n_coils : int
        Number of coils.
    """
    N = conductor_distribution.size
    possible_connections = obtain_connection(conductor_distribution)

    path = []
    path_ = []
    coil_pitch_list = []

    for i in range(len(possible_connections)):
        temp = np.abs(np.diff(possible_connections[i]))
        temp[temp > N / 2] = np.abs(N - temp[temp > N / 2])
        coil_pitch_list.append(temp)
        path.append(np.sum(temp))
        a = np.unique(temp)
        path_.append(np.sum(temp) + a.size)

    optimal = np.array(possible_connections[np.argmin(path_)]).astype(int)

    set_of_connection = []
    for i in range(optimal.size - 1):
        if i % 2:
            set_of_connection.append([optimal[i + 1], optimal[i]])
        else:
            set_of_connection.append([optimal[i], optimal[i + 1]])
    set_of_connection = np.array(set_of_connection)

    set_of_coil_pitch = coil_pitch_list[np.argmin(path_)]
    n_coils = set_of_connection.shape[0]

    return set_of_connection, set_of_coil_pitch, n_coils


def obtain_mcoil_connection(conductor_distribution):
    """Multi-coil connection: pair positive and negative conductors
    with similar magnitudes (minimal deviation).

    Parameters
    ----------
    conductor_distribution : ndarray
        Integer conductor distribution vector.

    Returns
    -------
    set_of_connection : ndarray
        Array of shape (n_coils, 2) with [positive, negative] indices.
    set_of_coil_pitch : ndarray
        Coil pitch for each connection.
    n_coils : int
        Number of coils.
    """
    N = conductor_distribution.size
    idx_p = np.where(conductor_distribution > 0)[0]
    idx_p = idx_p[np.argsort(conductor_distribution[idx_p])][::-1]
    idx_n = np.where(conductor_distribution < 0)[0]

    connection = []
    for i in range(idx_p.size):
        idx_p_current = idx_p[i]
        idx_n_match = idx_n[np.argmin(
            np.abs(conductor_distribution[idx_n] + conductor_distribution[idx_p_current]))]
        connection.append([idx_p_current, idx_n_match])
        idx_n = idx_n[np.where(np.logical_not(idx_n_match == idx_n))]
        if idx_n.size == 0:
            break

    set_of_connection = np.array(connection)
    set_of_coil_pitch = coil_pitch(set_of_connection[:, 0], set_of_connection[:, 1], N)
    n_coils = set_of_connection.shape[0]

    return set_of_connection, set_of_coil_pitch, n_coils


def obtain_mcond_connection(conductor_distribution):
    """Multi-conductor connection: shortest path with minimal unique pitches.

    Parameters
    ----------
    conductor_distribution : ndarray
        Integer conductor distribution vector.

    Returns
    -------
    set_of_connection : ndarray
        Array of shape (n_coils, 2) with [positive, negative] indices.
    set_of_coil_pitch : ndarray
        Coil pitch for each connection.
    n_coils : int
        Number of coils.
    """
    N = conductor_distribution.size
    idx_p_ = np.where(conductor_distribution > 0)[0]
    idx_n_ = np.where(conductor_distribution < 0)[0]

    possible_connections = []
    for j in range(idx_p_.size):
        idx_p = np.roll(idx_p_, j)
        idx_n = idx_n_.copy()
        connection = []
        for i in range(idx_p.size):
            idx_p_current = idx_p[i]
            idx_n_match = idx_n[np.argmin(coil_pitch(idx_n, idx_p_current, N))]
            connection.append([idx_p_current, idx_n_match])
            idx_n = idx_n[np.where(np.logical_not(idx_n_match == idx_n))]
            if idx_n.size == 0:
                break
        possible_connections.append(connection)

    path_ = []
    coil_pitch_list = []
    for i in range(len(possible_connections)):
        temp = np.abs(np.diff(np.array(possible_connections[i])[:, 0:2], axis=1))
        temp[temp > N / 2] = np.abs(N - temp[temp > N / 2])
        coil_pitch_list.append(temp)
        a = np.unique(temp)
        path_.append(np.sum(temp) + a.size)

    best = np.argmin(path_)
    set_of_connection = np.array(possible_connections[best]).astype(int)
    set_of_coil_pitch = np.array(coil_pitch_list[best])
    n_coils = set_of_connection.shape[0]

    return set_of_connection, set_of_coil_pitch, n_coils


# ============================================================================
# Internal: common template for winding topology derivation
# ============================================================================

def _build_connection_matrix(conn_vec, n_slots, n_coils_extra=0):
    """Build a connection matrix from a connection vector (coil indices).

    Parameters
    ----------
    conn_vec : ndarray
        Array of shape (n_coils, 2) with [positive, negative] slot indices.
    n_slots : int
        Number of slots.
    n_coils_extra : int
        Extra columns for multi-conductor common conductor.

    Returns
    -------
    ndarray
        Connection matrix of shape (n_slots, n_coils + n_coils_extra).
    """
    n_coils = conn_vec.shape[0]
    conn_matrix = np.zeros((n_slots, n_coils + n_coils_extra))
    for i in range(n_coils):
        conn_matrix[conn_vec[i, 0], i] = 1
        conn_matrix[conn_vec[i, 1], i] = -1
    return conn_matrix


def _integer_cond_ideal(connection_vector):
    """Convert a float conductor distribution to a scaled integer array.

    Parameters
    ----------
    connection_vector : ndarray
        Float conductor distribution vector.

    Returns
    -------
    ndarray
        Integer conductor distribution (scaled by N * _CONDUCTOR_INT_SCALE).
    """
    N = connection_vector.size
    return np.rint(connection_vector * N * _CONDUCTOR_INT_SCALE).astype(int)


def _build_topo_from_coil_group(coil_group, connection_fn, is_sp=False):
    """Template for winding topology derivation from a coil group.

    Parameters
    ----------
    coil_group : CoilGroup
        Primitive coil group.
    connection_fn : callable
        Function that takes (cond_ideal) and returns
        (conn_vec, pitch_vec, n_coils).
    is_sp : bool
        If True, use single-way shortest-path logic (multi-conductor).

    Returns
    -------
    PriMultiLayerTurnPitchTopo
        Resulting winding topology.
    """
    a = coil_group

    cond_ideal = _integer_cond_ideal(a.connection_vector)
    conn_vec, pitch_vec, n_coils = connection_fn(cond_ideal)

    if not is_sp:
        # Standard: double-way or multi-coil
        conn_matrix = _build_connection_matrix(conn_vec, cond_ideal.size)
        n_turns, error, cond_real = calculate_number_of_turns(conn_matrix, cond_ideal)
        multi_cond_matrix = 0
    else:
        # Multi-conductor (SP): extra common conductor column
        conn_matrix = _build_connection_matrix(conn_vec, cond_ideal.size, n_coils_extra=1)
        multi_cond_matrix = np.zeros((cond_ideal.size, n_coils))

        for i in range(n_coils):
            conn_matrix[conn_vec[i, 1], -1] = np.sign(
                np.sum(cond_ideal[conn_vec[i, :]]))
            multi_cond_matrix[conn_vec[i, 1], i] = np.sign(
                np.sum(cond_ideal[conn_vec[i, :]]))

        n_turns, error, cond_real = calculate_number_of_turns(conn_matrix, cond_ideal)

        # Normalize by common conductor turns
        if n_turns[-1] != 0:
            n_turns = n_turns / n_turns[-1]
        n_turns = np.rint(n_turns)
        cond_real = conn_matrix.dot(n_turns)

        conn_matrix = conn_matrix[:, :-1]
        n_turns = n_turns[:-1]

        error_abs = cond_real * n_turns[-1] - cond_ideal
        error = LA.norm(error_abs.astype(float)) / LA.norm(cond_ideal.astype(float))

    return PriMultiLayerTurnPitchTopo(
        cond_ideal, cond_real, conn_vec, pitch_vec, conn_matrix,
        n_turns, error, multi_cond_matrix=multi_cond_matrix,
        msym_matrix=a.mirror_symmetry_matrix,
        rsym_matrix_i=a.rotation_symmetry_matrix,
        rsym_matrix_ii=a.rotation_symmetry_matrix_type_ii,
        m_pha_curr_sys=a.current_system,
        _msym_matrix=a._mirror_symmetry_matrix,
        working_harmonic=a.working_harmonic)


# ============================================================================
# Winding topology derivation functions
# ============================================================================

def winding_topology_double_way_connection(coil_groups):
    """Derive winding topologies using double-way connection
    (multi-layer topology approximation).

    Parameters
    ----------
    coil_groups : list of CoilGroup
        Primitive coil groups.

    Returns
    -------
    list of PriMultiLayerTurnPitchTopo
        Resulting winding topologies.
    """
    return [_build_topo_from_coil_group(a, obtain_set_of_connection)
            for a in coil_groups]


def winding_topology_single_way_connection_md(coil_groups):
    """Derive winding topologies using single-way connection
    with minimal deviation (multi-coil approach).

    Parameters
    ----------
    coil_groups : list of CoilGroup
        Primitive coil groups.

    Returns
    -------
    list of PriMultiLayerTurnPitchTopo
        Resulting winding topologies.
    """
    return [_build_topo_from_coil_group(a, obtain_mcoil_connection)
            for a in coil_groups]


def winding_topology_single_way_connection_sp(coil_groups):
    """Derive winding topologies using single-way connection
    with shortest path (multi-conductor approach).

    Parameters
    ----------
    coil_groups : list of CoilGroup
        Primitive coil groups.

    Returns
    -------
    list of PriMultiLayerTurnPitchTopo
        Resulting winding topologies.
    """
    return [_build_topo_from_coil_group(a, obtain_mcond_connection, is_sp=True)
            for a in coil_groups]


# ============================================================================
# Post-processing: derive standard winding types
# ============================================================================

def obtain_multi_turn_winding_topology(primitive_topologies):
    """Derive multi-turn winding topology by selecting coils with the
    most common coil pitch.

    Parameters
    ----------
    primitive_topologies : list of PriMultiLayerTurnPitchTopo
        Primitive winding topologies.

    Returns
    -------
    list of PriMultiLayerTurnPitchTopo
        Multi-turn winding topologies.
    """
    results = []
    for topo in primitive_topologies:
        pitch = topo.coil_pitch
        unique_pitch, _, counts = np.unique(pitch, return_counts=True, return_inverse=True)
        best_pitch = unique_pitch[np.argmax(counts)]
        idx = np.where(pitch == best_pitch)[0]

        conn_matrix = topo.connection_matrix[:, idx]
        conn_vec = topo.connection_vector[idx, :]
        coil_pitch = topo.coil_pitch[idx]
        cond_ideal = topo.conductor_distribution_ideal

        n_turns, error, cond_real = calculate_number_of_turns(conn_matrix, cond_ideal)

        result = PriMultiLayerTurnPitchTopo(
            cond_ideal, cond_real, conn_vec, coil_pitch, conn_matrix,
            n_turns, error,
            msym_matrix=topo.msym_matrix, rsym_matrix_i=topo.rsym_matrix_i,
            rsym_matrix_ii=topo.rsym_matrix_ii, m_pha_curr_sys=topo.m_pha_curr_sys,
            _msym_matrix=topo._msym_matrix, working_harmonic=topo.working_harmonic)
        results.append(result)

    return results


def obtain_multi_layer_winding_topology(multi_turn_topologies):
    """Derive multi-layer winding topology from multi-turn topologies
    by normalizing turns to the minimum.

    Parameters
    ----------
    multi_turn_topologies : list of PriMultiLayerTurnPitchTopo
        Multi-turn winding topologies.

    Returns
    -------
    list of PriMultiLayerTurnPitchTopo
        Multi-layer winding topologies.
    """
    results = []
    for topo in multi_turn_topologies:
        n_turns = topo.n_turns
        n_turns = np.rint(n_turns / np.amin(n_turns)) * np.amin(n_turns)
        conn_matrix = topo.connection_matrix
        cond_real = conn_matrix.dot(n_turns)
        cond_ideal = topo.conductor_distribution_ideal

        error_abs = cond_real - cond_ideal
        error_rel = LA.norm(error_abs.astype(float)) / LA.norm(cond_ideal.astype(float))

        result = PriMultiLayerTurnPitchTopo(
            cond_ideal, cond_real, topo.connection_vector, topo.coil_pitch,
            conn_matrix, n_turns, error_rel,
            msym_matrix=topo.msym_matrix, rsym_matrix_i=topo.rsym_matrix_i,
            rsym_matrix_ii=topo.rsym_matrix_ii, m_pha_curr_sys=topo.m_pha_curr_sys,
            _msym_matrix=topo._msym_matrix, working_harmonic=topo.working_harmonic)
        results.append(result)

    return results


def obtain_double_layer_winding_topology(multi_coil_topologies):
    """Derive double-layer (single-turn) winding topology from multi-coil topologies.

    Parameters
    ----------
    multi_coil_topologies : list of PriMultiLayerTurnPitchTopo
        Multi-coil winding topologies.

    Returns
    -------
    list of PriMultiLayerTurnPitchTopo
        Double-layer winding topologies.
    """
    results = []
    for topo in multi_coil_topologies:
        pitch = topo.coil_pitch
        conn_matrix = np.sign(topo.connection_matrix)
        _conn_matrix = np.sum(conn_matrix, axis=1)
        cond_ideal = topo.conductor_distribution_ideal

        n_turns, error, cond_real = calculate_number_of_turns(
            np.atleast_2d(_conn_matrix).transpose(), cond_ideal)
        n_turns = n_turns * np.ones(pitch.size)

        result = PriMultiLayerTurnPitchTopo(
            cond_ideal, cond_real, topo.connection_vector, pitch,
            conn_matrix, n_turns, error,
            msym_matrix=topo.msym_matrix, rsym_matrix_i=topo.rsym_matrix_i,
            rsym_matrix_ii=topo.rsym_matrix_ii, m_pha_curr_sys=topo.m_pha_curr_sys,
            _msym_matrix=topo._msym_matrix, working_harmonic=topo.working_harmonic)
        results.append(result)

    return results


def obtain_single_layer_winding_topology(multi_turn_topologies):
    """Derive single-layer winding topology from multi-turn topologies.

    Selects the coils with the largest number of turns (upper half).

    Parameters
    ----------
    multi_turn_topologies : list of PriMultiLayerTurnPitchTopo
        Multi-turn winding topologies.

    Returns
    -------
    list of PriMultiLayerTurnPitchTopo
        Single-layer winding topologies.
    """
    results = []
    for topo in multi_turn_topologies:
        n_turns = topo.n_turns
        idx_sorted = np.argsort(n_turns)
        idx_keep = idx_sorted[int(n_turns.size / 2):]

        pitch = topo.coil_pitch[idx_keep]
        conn_matrix = np.sign(topo.connection_matrix[:, idx_keep])
        _conn_matrix = np.sum(conn_matrix, axis=1)
        cond_ideal = topo.conductor_distribution_ideal

        n_turns, error, cond_real = calculate_number_of_turns(
            np.atleast_2d(_conn_matrix).transpose(), cond_ideal)
        n_turns = n_turns * np.ones(pitch.size)

        result = PriMultiLayerTurnPitchTopo(
            cond_ideal, cond_real, topo.connection_vector[idx_keep, :],
            pitch, conn_matrix, n_turns, error,
            msym_matrix=topo.msym_matrix, rsym_matrix_i=topo.rsym_matrix_i,
            rsym_matrix_ii=topo.rsym_matrix_ii, m_pha_curr_sys=topo.m_pha_curr_sys,
            _msym_matrix=topo._msym_matrix, working_harmonic=topo.working_harmonic)
        results.append(result)

    return results


# ============================================================================
# Legacy / utility functions
# ============================================================================

def get_number_of_layer(set_of_coil, mirror_symmetry_matrix,
                        rotation_symmetry_matrix, matrix_of_rotation_symmetry_type_ii,
                        single_turn_multi_turn):
    """Calculate the number of winding layers.

    Parameters
    ----------
    set_of_coil : ndarray
        Coil connection set.
    mirror_symmetry_matrix : ndarray
        Mirror symmetry matrix.
    rotation_symmetry_matrix : ndarray
        Rotation symmetry matrix (type I).
    matrix_of_rotation_symmetry_type_ii : ndarray
        Rotation symmetry matrix (type II).
    single_turn_multi_turn : str
        'MultiTurn' or 'SingleTurn' mode.

    Returns
    -------
    int
        Number of winding layers.
    """
    set_of_coil = set_of_coil.copy()
    if single_turn_multi_turn == 'MultiTurn':
        set_of_coil[np.abs(set_of_coil) > 1e-6] = 1
    if single_turn_multi_turn == 'SingleTurn':
        mask = np.abs(set_of_coil) > 1e-6
        set_of_coil[mask] = set_of_coil[mask] / np.amin(np.abs(set_of_coil[mask]))

    conn_matrices = []
    for i in range(np.size(set_of_coil, axis=1)):
        cm = connection_vector_to_connection_matrix(
            set_of_coil[:, i], mirror_symmetry_matrix,
            rotation_symmetry_matrix, matrix_of_rotation_symmetry_type_ii)
        conn_matrices.append(cm)

    conn_matrices = np.abs(np.array(conn_matrices))
    return int(np.max(np.sum(conn_matrices, axis=(0, 2))))


def get_number_of_unique_pitch(coils):
    """Count unique coil pitches across a set of coils.

    Parameters
    ----------
    coils : list of Coil
        List of coil objects.

    Returns
    -------
    int
        Number of unique pitches.
    """
    pitches = coils[0].pitch
    for j in range(1, len(coils)):
        pitches = np.append(pitches, coils[j].pitch)
    return np.unique(pitches).size


def get_unique_winding_spectrum(set_of_winding_spectra):
    """Find indices of unique winding spectra.

    Parameters
    ----------
    set_of_winding_spectra : list of ndarray
        List of winding spectrum arrays.

    Returns
    -------
    ndarray
        Indices of unique spectra.
    """
    def sum_str_vector(sv):
        result = sv[0]
        for i in range(1, sv.size):
            result = result + sv[i]
        return result

    ws = (np.abs(set_of_winding_spectra[0]) * 1e4).astype(int).astype(str)
    ws = sum_str_vector(ws)
    matrix = ws
    for i in range(1, len(set_of_winding_spectra)):
        ws = (np.abs(set_of_winding_spectra[i]) * 1e4).astype(int).astype(str)
        ws = sum_str_vector(ws)
        matrix = np.hstack((matrix, ws))

    _, idx = np.unique(matrix, return_index=True)
    return idx.astype(int)


def classify_set_of_coil(set_of_coil):
    """Classify coils by pitch, winding factor, and spectrum type.

    Returns a nested list structure for topology selection.

    Parameters
    ----------
    set_of_coil : list of list of Coil
        Nested list of coil objects.

    Returns
    -------
    list of list of dict
        Each dict has keys: 'type', 'value', 'coils'.
    """
    n_types = len(set_of_coil)
    all_categories = []

    for n in range(n_types):
        n_coils = len(set_of_coil[n])
        categories = []

        pitches = np.zeros(n_coils)
        spectra = np.zeros((np.size(set_of_coil[n][0].winding_spectrum), n_coils), dtype=np.complex_)
        spectrum_types = np.zeros(n_coils)
        factors = np.zeros(n_coils)

        for k in range(n_coils):
            pitches[k] = set_of_coil[n][k].pitch
            spectra[:, k] = set_of_coil[n][k].winding_spectrum
            wf = np.abs(set_of_coil[n][k].winding_spectrum)
            wf_type = wf.copy()
            wf_type[wf_type < 1e-6] = 0
            wf_type[wf_type > 1e-6] = 1
            spectrum_types[k] = int(''.join(wf_type.astype(int).astype(str)))
            factors[k] = int(''.join((np.abs(spectra[:, k] * 1e4).astype(int).astype(str))))

        # By coil pitch
        for p in np.unique(pitches):
            ii = np.where(pitches == p)[0]
            same_coils = [set_of_coil[n][int(i)] for i in ii]
            categories.append({'type': 'pitch', 'value': p, 'coils': same_coils})

        all_categories.append(categories)

    return all_categories


def category_of_coil_to_multiphase_winding(category_of_coil, set_of_multiphase_winding):
    """Convert a category of coils to a modified multi-phase winding topology.

    .. note::
        This is a legacy function. For new code, use the design pipeline
        (get_coil -> modification functions) directly.

    Parameters
    ----------
    category_of_coil : CategoryOfCoil
        Category of coils.
    set_of_multiphase_winding : list
        Multi-phase winding set (unused, kept for API compatibility).

    Returns
    -------
    ModifiedMultiPhaseWinding
        Modified multi-phase winding topology.
    """
    from winding.models import ModifiedMultiPhaseWinding
    coils = category_of_coil.set_of_coil

    b = (coils[0].parent_coil_group.connection_vector * 1E3).astype(int)
    cv0 = (coils[0].connection_vector * 1E3).astype(int)
    A = np.sign(cv0)

    y_scalar = np.sign(np.sum(cv0))
    n2 = np.where(cv0 < 0)[0][0]
    A_ = np.sum(cv0)
    b_ = -1 * y_scalar * cv0[n2]

    A = np.atleast_2d(A)
    b = np.atleast_2d(b)
    A_ = np.atleast_2d(A_)
    b_ = np.atleast_2d(b_)

    for j in range(1, len(coils)):
        cvj = (coils[j].connection_vector * 1E3).astype(int)
        A = np.vstack((A, np.sign(cvj)))
        y_scalar = np.sign(np.sum(cvj))
        n2 = np.where(cvj < 0)[0][0]
        A_ = np.vstack((A_, np.sum(cvj)))
        b_ = np.vstack((b_, -1 * y_scalar * cvj[n2]))

    A = np.transpose(A)
    b = np.transpose(b)

    # Single-turn solution
    x = LA.lstsq(A, b)[0]
    x_single = np.rint(x / np.min(x)) * np.min(x)
    error = A.dot(x_single) - b
    r_single = LA.norm(error) / LA.norm(b)

    winding = ModifiedMultiPhaseWinding()
    winding.set_of_coil = A[:, :] * x_single[:, 0]
    winding.connection_vector = (A.dot(x_single))[:, 0]
    winding.current_system = coils[0].parent_coil_group.current_system
    winding.mirror_symmetry_matrix = coils[0].parent_coil_group.mirror_symmetry_matrix
    winding._mirror_symmetry_matrix = coils[0].parent_coil_group._mirror_symmetry_matrix
    winding.rotation_symmetry_matrix = coils[0].parent_coil_group.rotation_symmetry_matrix
    winding.matrix_of_rotation_symmetry_type_ii = coils[0].parent_coil_group.rotation_symmetry_matrix_type_ii
    winding.has_rotation_symmetry = coils[0].parent_coil_group.parent_single_phase_winding.has_symmetry
    winding.has_mirror_symmetry = coils[0].parent_coil_group.has_symmetry

    from winding.design import get_property_of_coil
    _, winding.connection_matrix, winding.winding_spectrum = get_property_of_coil(
        winding.connection_vector,
        winding.mirror_symmetry_matrix,
        winding.rotation_symmetry_matrix,
        winding.matrix_of_rotation_symmetry_type_ii,
        winding.current_system)

    winding.n_layers = get_number_of_layer(
        winding.set_of_coil, winding.mirror_symmetry_matrix,
        winding.rotation_symmetry_matrix,
        winding.matrix_of_rotation_symmetry_type_ii, 'SingleTurn')
    winding.n_total_conductors = np.sum(np.abs(winding.connection_matrix))
    winding.set_of_coil = winding.set_of_coil / winding.n_total_conductors
    winding.connection_vector = winding.connection_vector / winding.n_total_conductors
    winding.error = r_single

    return winding
