"""
Winding topology design functions.

Functions for the step-by-step design of winding topologies from
ideal winding factor harmonic spectra to realizable winding configurations.

Design pipeline:
    Ideal Spectrum → MMF → Primitive Multi-Phase Winding
    → Single-Phase Winding (rotation symmetry)
    → Coil Group (mirror symmetry)
    → Coils

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import numpy as np
from numpy import linalg as LA
from winding.models import (WindingSpectrum, CurrentSystem, MMF,
                            MultiPhaseWinding, SinglePhaseWinding,
                            CoilGroup, Coil)
from winding.analysis import winding_topology_to_spectrum, get_mmf
from winding.utils import proj, calc_connection
from winding.transforms import (detect_mirror_symmetry, get_part_of_mirror_symmetry,
                                detect_rotation_symmetry)


def get_primitive_multiphase_winding(ideal_mmf_obj, current_system_obj):
    """
    Obtain the primitive multi-phase winding topology from the ideal MMF
    distribution and the multi-phase current system.

    Two types of connection matrices are generated (differing by a rotation
    angle delta).

    Parameters
    ----------
    ideal_mmf_obj : MMF
        Object containing the ideal normalized MMF distribution.
    current_system_obj : CurrentSystem
        Object containing the symmetrical multi-phase current system.

    Returns
    -------
    list of MultiPhaseWinding
        Two primitive multi-phase winding topologies.
    """
    ideal_mmf = ideal_mmf_obj.distribution
    current_system = current_system_obj.distribution
    n_mmf_phasors = np.size(ideal_mmf)
    n_phases = current_system_obj.n_phases

    n_connection_types = 2

    if n_mmf_phasors % 2:
        angle_delta = np.exp(1j * np.pi / (2 * n_mmf_phasors))
    else:
        angle_delta = np.exp(1j * np.pi / n_mmf_phasors)

    windings = []
    for h in range(n_connection_types):
        connection_matrix = np.zeros((n_mmf_phasors, n_phases))
        current_system_ = current_system * (angle_delta ** h)

        for n in range(n_mmf_phasors):
            mmf_n = ideal_mmf[n]
            k0, k1 = proj(current_system_, mmf_n)
            ck0, ck1 = calc_connection(mmf_n, current_system_, k0, k1)
            connection_matrix[n, int(k0)] = ck0[0]
            connection_matrix[n, int(k1)] = ck1[0]

        winding = MultiPhaseWinding(ideal_mmf_obj, current_system_)
        connection_matrix[np.abs(connection_matrix) < 1E-6] = 0
        winding.connection_matrix = connection_matrix
        windings.append(winding)

    return windings


def get_single_phase_winding(multi_phase_windings, current_system_flag):
    """
    Obtain primitive single-phase winding topologies by detecting
    rotational symmetry in the multi-phase winding.

    Parameters
    ----------
    multi_phase_windings : list of MultiPhaseWinding
        Primitive multi-phase windings.
    current_system_flag : int
        0 for source current, 1 for winding design current.

    Returns
    -------
    list of SinglePhaseWinding
        Single-phase winding topologies.
    """
    single_phase_windings = []

    for winding in multi_phase_windings:
        connection_matrix = winding.connection_matrix

        has_symmetry = 0
        N = np.size(connection_matrix, axis=0)
        m = np.size(connection_matrix, axis=1)

        n1 = np.linspace(0, N, N, endpoint=False, dtype=int)
        n2 = np.linspace(0, m, m, endpoint=False, dtype=int)

        matrix_of_rotation_symmetry = np.zeros((N, N))
        matrix_of_rotation_symmetry_type_ii = np.zeros((N, N))
        connection_vector = np.zeros(N)

        for g in range(1, N):
            if has_symmetry == 1:
                break
            for h in range(1, m):
                k1 = np.mod(n1 + g, N)
                k2 = np.mod(n2 + h, m)

                matrix_of_rotation_symmetry_type_i = np.zeros((N, N))
                matrix_of_rotation_symmetry_type_ii_ = np.zeros((m, m))
                matrix_of_rotation_symmetry_type_i[n1, k1] = 1
                matrix_of_rotation_symmetry_type_ii_[n2, k2] = 1

                connection_matrix_ = connection_matrix.copy()
                if current_system_flag == 1:
                    connection_matrix_[:, 0] = -connection_matrix_[:, 0]

                residual = connection_matrix_ - matrix_of_rotation_symmetry_type_i.dot(
                    connection_matrix).dot(matrix_of_rotation_symmetry_type_ii_)

                if LA.norm(residual, np.inf) < 1E-10:
                    has_symmetry = 1
                    matrix_of_rotation_symmetry = matrix_of_rotation_symmetry_type_i
                    matrix_of_rotation_symmetry_type_ii = matrix_of_rotation_symmetry_type_ii_
                    connection_vector = connection_matrix[:, 0]
                    break

        single_winding = SinglePhaseWinding(winding)
        single_winding.connection_vector = connection_vector
        single_winding.rotation_symmetry_matrix = matrix_of_rotation_symmetry
        single_winding.rotation_symmetry_matrix_type_ii = matrix_of_rotation_symmetry_type_ii
        single_winding.has_symmetry = has_symmetry
        single_phase_windings.append(single_winding)

    return single_phase_windings


def get_coil_group(single_phase_windings):
    """
    Obtain primitive coil groups by detecting mirror symmetry
    in the single-phase winding.

    Parameters
    ----------
    single_phase_windings : list of SinglePhaseWinding
        Single-phase winding topologies.

    Returns
    -------
    list of CoilGroup
        Coil group topologies.
    """
    coil_groups = []

    for spw in single_phase_windings:
        connection_vector = spw.connection_vector
        has_symmetry, msym_matrix, position = detect_mirror_symmetry(connection_vector)

        if has_symmetry == 1:
            upper_part, _msym_matrix = get_part_of_mirror_symmetry(
                msym_matrix, position, connection_vector, 'U')
        else:
            upper_part = connection_vector
            msym_matrix = _msym_matrix = np.identity(np.size(connection_vector))

        cg = CoilGroup(spw)
        cg.connection_vector = upper_part
        cg.has_symmetry = has_symmetry
        cg.mirror_symmetry_matrix = _msym_matrix
        cg._mirror_symmetry_matrix = msym_matrix
        cg.position_of_symmetry_axis = position
        coil_groups.append(cg)

    return coil_groups


def find_out_possible_coils(mirror_symmetry_part):
    """
    Enumerate all possible coil combinations from a mirror-symmetric
    conductor distribution.

    A coil connects one positive conductor and one negative conductor.

    Parameters
    ----------
    mirror_symmetry_part : ndarray
        The upper (or lower) part of the mirror-symmetric distribution.

    Returns
    -------
    n_possible_coils : int
        Number of possible coil combinations.
    container_of_possible_coils : ndarray
        Matrix where each column is a possible coil.
    """
    N = np.size(mirror_symmetry_part, axis=0)
    mirror_symmetry_part[np.abs(mirror_symmetry_part) < 1e-6] = 0

    idx_pos = np.nonzero(mirror_symmetry_part > 0)[0]
    idx_neg = np.nonzero(mirror_symmetry_part < 0)[0]
    n_possible_coils = idx_pos.size * idx_neg.size

    container = np.zeros((N, n_possible_coils))
    k = 0
    for n1 in idx_pos:
        for n2 in idx_neg:
            container[[n1, n2], k] = mirror_symmetry_part[[n1, n2]]
            k += 1

    return n_possible_coils, container


def get_property_of_coil(connection_vector_of_coil,
                          matrix_of_mirror_symmetry,
                          matrix_of_rotation_symmetry,
                          matrix_of_rotation_symmetry_type_ii,
                          multi_phase_current_system):
    """
    Calculate the properties (pitch, connection matrix, winding spectrum)
    of a single coil.

    Parameters
    ----------
    connection_vector_of_coil : ndarray
        The coil's connection vector.
    matrix_of_mirror_symmetry : ndarray
        Mirror symmetry matrix.
    matrix_of_rotation_symmetry : ndarray
        Rotation symmetry matrix (type I).
    matrix_of_rotation_symmetry_type_ii : ndarray
        Rotation symmetry matrix (type II).
    multi_phase_current_system : ndarray
        Multi-phase current system.

    Returns
    -------
    coil_pitch : int
        The coil pitch.
    connection_matrix : ndarray
        The multi-phase connection matrix.
    winding_spectrum : ndarray
        The winding factor harmonic spectrum.
    """
    n_phases = np.size(multi_phase_current_system)
    n_slots = np.size(connection_vector_of_coil)

    # Coil pitch
    n1 = np.nonzero(connection_vector_of_coil > 0)[0][0]
    n2 = np.nonzero(connection_vector_of_coil < 0)[0][0]
    pitch1 = np.mod(n1 - n2, n_slots)
    pitch2 = np.mod(n2 - n1, n_slots)
    coil_pitch = np.min([pitch1, pitch2])

    # Connection matrix via mirror symmetry
    connection_vector = matrix_of_mirror_symmetry.dot(connection_vector_of_coil)
    connection_matrix_ = np.zeros((n_slots, n_phases))
    connection_matrix_[:, 0] = connection_vector
    connection_matrix = connection_matrix_
    for k in range(1, n_phases):
        connection_matrix = connection_matrix + LA.matrix_power(
            matrix_of_rotation_symmetry, k).dot(connection_matrix_).dot(
                LA.matrix_power(matrix_of_rotation_symmetry_type_ii, k))

    winding_spectrum = winding_topology_to_spectrum(connection_matrix, multi_phase_current_system)

    return coil_pitch, connection_matrix, winding_spectrum


def get_coil(coil_groups):
    """
    Generate all possible coils for each coil group.

    Parameters
    ----------
    coil_groups : list of CoilGroup
        Coil group topologies.

    Returns
    -------
    list of list of Coil
        All possible coils for each connection matrix type.
    """
    all_coils = []

    for cg in coil_groups:
        upper_part = cg.connection_vector
        msym_matrix = cg.mirror_symmetry_matrix
        rsym_matrix_i = cg.parent_single_phase_winding.rotation_symmetry_matrix
        rsym_matrix_ii = cg.parent_single_phase_winding.rotation_symmetry_matrix_type_ii
        current_system = cg.parent_single_phase_winding.parent_multi_phase_winding.current_system

        _, container = find_out_possible_coils(upper_part)

        coils = []
        for k in range(container.shape[1]):
            cv = container[:, k]
            pitch, cm, ws = get_property_of_coil(
                cv, msym_matrix, rsym_matrix_i, rsym_matrix_ii, current_system)

            coil_obj = Coil(cg)
            coil_obj.connection_vector = cv
            coil_obj.pitch = pitch
            coil_obj.connection_matrix = cm
            coil_obj.winding_spectrum = ws
            coils.append(coil_obj)

        all_coils.append(coils)

    return all_coils
