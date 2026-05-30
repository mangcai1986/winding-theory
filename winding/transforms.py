"""
Transformation and symmetry detection functions.

Rotation symmetry detection and mirror symmetry detection for
winding topology matrices and vectors.

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import numpy as np
from numpy import linalg as LA


def detect_rotation_symmetry(connection_matrix):
    """
    Detect rotational symmetry of a connection matrix.

    Finds the smallest rotation (g, h) such that the matrix is invariant
    under simultaneous rotation of slot and phase indices.

    Parameters
    ----------
    connection_matrix : ndarray
        Connection matrix of shape (n_slots, n_phases).

    Returns
    -------
    has_symmetry : int
        1 if symmetry found, 0 otherwise.
    matrix_of_rotation_symmetry : ndarray
        The rotation matrix (n_slots x n_slots).
    connection_vector : ndarray
        The first phase column vector.
    """
    has_symmetry = 0
    N = np.size(connection_matrix, axis=0)
    m = np.size(connection_matrix, axis=1)

    n1 = np.linspace(0, N, N, endpoint=False, dtype=int)
    n2 = np.linspace(0, m, m, endpoint=False, dtype=int)

    matrix_of_rotation_symmetry = np.zeros((N, N))
    connection_vector = np.zeros(N)

    for g in range(1, N):
        if has_symmetry == 1:
            break
        for h in range(1, m):
            k1 = np.mod(n1 + g, N)
            k2 = np.mod(n2 + h, m)

            matrix_of_rotation_symmetry_type_i = np.zeros((N, N))
            matrix_of_rotation_symmetry_type_ii = np.zeros((m, m))
            matrix_of_rotation_symmetry_type_i[n1, k1] = 1
            matrix_of_rotation_symmetry_type_ii[n2, k2] = 1

            residum = connection_matrix - matrix_of_rotation_symmetry_type_i.dot(connection_matrix).dot(
                matrix_of_rotation_symmetry_type_ii)

            if LA.norm(residum, np.inf) < 1E-10:
                has_symmetry = 1
                matrix_of_rotation_symmetry = matrix_of_rotation_symmetry_type_i
                connection_vector = connection_matrix[:, 0]
                break

    return has_symmetry, matrix_of_rotation_symmetry, connection_vector


def detect_mirror_symmetry(connection_vector):
    """
    Detect mirror symmetry of a connection vector.

    Finds the axis position g such that the vector is invariant
    under reflection.

    Parameters
    ----------
    connection_vector : ndarray
        Single-phase winding connection vector.

    Returns
    -------
    has_symmetry : int
        1 if symmetry found, 0 otherwise.
    matrix_of_mirror_symmetry : ndarray
        The mirror symmetry matrix.
    position_of_symmetry_axis : float
        Angular position of the symmetry axis.
    """
    has_symmetry = 0
    N = connection_vector.size
    matrix_of_mirror_symmetry = np.zeros((N, N))
    position_of_symmetry_axis = np.nan

    for g in range(0, N):
        matrix_of_mirror_symmetry = np.zeros((N, N))
        k = np.linspace(0, N, N, endpoint=False, dtype=int)
        n = np.mod(g - k, N)
        matrix_of_mirror_symmetry[n, k] = 1

        residum = connection_vector - matrix_of_mirror_symmetry.dot(connection_vector)
        if LA.norm(residum, np.inf) < 1E-6:
            has_symmetry = 1
            position_of_symmetry_axis = g
            break

    return has_symmetry, matrix_of_mirror_symmetry, position_of_symmetry_axis


def get_part_of_mirror_symmetry(matrix_of_mirror_symmetry, position_of_symmetry_axis,
                                 connection_vector, flag_of_part='U'):
    """
    Extract the upper or lower part of a mirror-symmetric vector.

    Parameters
    ----------
    matrix_of_mirror_symmetry : ndarray
        Mirror symmetry matrix.
    position_of_symmetry_axis : int
        Position of the symmetry axis.
    connection_vector : ndarray
        The connection vector.
    flag_of_part : str
        'U' for upper part, 'L' for lower part.

    Returns
    -------
    x : ndarray
        The extracted part.
    A : ndarray
        The combined matrix (I + mirror part).
    """
    N = connection_vector.size
    I = np.identity(N)
    A = np.zeros((N, N))

    if position_of_symmetry_axis % 2:  # odd
        index_u = np.arange(int(N / 2)) + int(np.ceil(position_of_symmetry_axis / 2))
    else:  # even
        index_u = np.arange(int(N / 2) + 1) + int(np.ceil(position_of_symmetry_axis / 2))
    index_l = index_u + int(N / 2)

    index_u = np.mod(index_u, N)
    index_l = np.mod(index_l, N)

    if flag_of_part == 'U':
        A[:, index_u] = matrix_of_mirror_symmetry[:, index_u]
    elif flag_of_part == 'L':
        A[:, index_l] = matrix_of_mirror_symmetry[:, index_l]

    A = I + A
    x = LA.solve(A, connection_vector)
    x[np.abs(x) / np.amax(np.abs(x)) < 1e-3] = 0
    return x, A


def connection_vector_to_connection_matrix(connection_vector,
                                            matrix_of_mirror_symmetry,
                                            matrix_of_rotation_symmetry,
                                            matrix_of_rotation_symmetry_type_ii):
    """
    Reconstruct the full multi-phase connection matrix from a single-phase
    connection vector using rotation and mirror symmetry.

    Parameters
    ----------
    connection_vector : ndarray
        Single-phase connection vector.
    matrix_of_mirror_symmetry : ndarray
        Mirror symmetry matrix.
    matrix_of_rotation_symmetry : ndarray
        Rotation symmetry matrix (type I).
    matrix_of_rotation_symmetry_type_ii : ndarray
        Rotation symmetry matrix (type II).

    Returns
    -------
    ndarray
        Full multi-phase connection matrix.
    """
    n_phases = np.size(matrix_of_rotation_symmetry_type_ii, axis=0)
    n_slots = np.size(connection_vector)

    connection_matrix_ = np.zeros((n_slots, n_phases))
    connection_matrix_[:, 0] = matrix_of_mirror_symmetry.dot(connection_vector)
    connection_matrix = connection_matrix_
    for k in range(1, n_phases):
        connection_matrix = connection_matrix + LA.matrix_power(matrix_of_rotation_symmetry, k).dot(
            connection_matrix_).dot(LA.matrix_power(matrix_of_rotation_symmetry_type_ii, k))

    return connection_matrix
