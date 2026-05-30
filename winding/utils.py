"""
Utility functions for winding topology operations.

Helper functions for projection, connection calculation, coil pitch,
and linear algebra operations.

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import numpy as np
from numpy import linalg as LA


def proj(multi_phase_current_system, mmf_n, n=2):
    """
    Find the two phase current vectors that best approximate a given MMF phasor.

    Returns the indices of the two closest phase currents.

    Parameters
    ----------
    multi_phase_current_system : ndarray
        Complex array of phase currents.
    mmf_n : complex
        The MMF phasor to project.
    n : int
        Number of projections (default 2).

    Returns
    -------
    k0 : int
        Index of the first best-matching phase.
    k1 : int
        Index of the second best-matching phase.
    """
    x = np.argsort(np.abs(np.real(multi_phase_current_system / mmf_n)))
    x = x[::-1]
    return x[0], x[1]


def calc_connection(mmf_n, multi_phase_current_system, k0, k1):
    """
    Calculate the connection coefficients for a given MMF phasor
    projected onto two phase current vectors.

    Parameters
    ----------
    mmf_n : complex
        The MMF phasor.
    multi_phase_current_system : ndarray
        Complex array of phase currents.
    k0 : int
        Index of first phase.
    k1 : int
        Index of second phase.

    Returns
    -------
    x0 : float
        Connection coefficient for phase k0.
    x1 : float
        Connection coefficient for phase k1.
    """
    bcomp = mmf_n
    b = np.vstack((np.real(bcomp), np.imag(bcomp)))
    acomp = multi_phase_current_system[[k0, k1]]
    A = np.vstack((np.real(acomp), np.imag(acomp)))
    x = LA.solve(A, b)

    x_out = np.around(x, decimals=10)

    # Handle equal-length case by adding a small perturbation
    if np.abs(x_out[0]) - np.abs(x_out[1]) == 0.:
        bcomp = mmf_n * np.exp(1j * 0.000001)
        b = np.vstack((np.real(bcomp), np.imag(bcomp)))
        x = LA.solve(A, b)
        x_out = np.around(x, decimals=10)

    return x_out[0], x_out[1]


def coil_pitch(a, b, N):
    """
    Calculate the coil pitch (shortest path) between two slot positions.

    Parameters
    ----------
    a : int or ndarray
        First slot index(es).
    b : int or ndarray
        Second slot index(es).
    N : int
        Total number of slots.

    Returns
    -------
    ndarray
        Coil pitch values.
    """
    pitch = np.abs(a - b)
    pitch[pitch > N / 2] = np.abs(N - pitch[pitch > N / 2])
    return pitch


def calculate_number_of_turns(connection_matrix, conductor_distribution):
    """
    Solve for the number of turns using least-squares approximation.

    Parameters
    ----------
    connection_matrix : ndarray
        Connection matrix of shape (n_slots, n_coils).
    conductor_distribution : ndarray
        Ideal conductor distribution vector.

    Returns
    -------
    n_turns : ndarray
        Integer number of turns per coil.
    error_rel : float
        Relative error of the approximation.
    conductor_distribution_real : ndarray
        Realized conductor distribution.
    """
    x = LA.lstsq(connection_matrix, conductor_distribution)
    n_turns = np.rint(x[0])
    n_turns = np.rint(n_turns)

    conductor_distribution_real = connection_matrix.dot(n_turns)
    error_abs = conductor_distribution_real - conductor_distribution
    error_rel = LA.norm(error_abs.astype(float)) / LA.norm(conductor_distribution.astype(float))

    return n_turns, error_rel, conductor_distribution_real


def normalize_cond_distri(cond_distri, m_cond_distri):
    """Normalize a conductor distribution using a multi-phase distribution."""
    m_cond_distri_ = np.sum(np.abs(m_cond_distri), axis=1)
    return np.rint(cond_distri / np.amax(m_cond_distri_) * 1e2).astype(int)


def s2m_cond_distri(s_cond_distri, rsym_matrix_i, rsym_matrix_ii):
    """Convert single-phase conductor distribution to multi-phase using symmetry."""
    n_phases = np.size(rsym_matrix_ii, axis=0)
    n_slots = np.size(rsym_matrix_i, axis=0)
    connection_matrix_of_coil_ = np.zeros((n_slots, n_phases))
    connection_matrix_of_coil_[:, 0] = s_cond_distri
    m_cond_distri = connection_matrix_of_coil_
    for k in range(1, n_phases):
        m_cond_distri = m_cond_distri + LA.matrix_power(rsym_matrix_i, k).dot(connection_matrix_of_coil_).dot(
            LA.matrix_power(rsym_matrix_ii, k))
    return m_cond_distri


def sum_str_vector(str_vector):
    """Concatenate a vector of strings into a single string."""
    result = str_vector[0]
    for i in range(1, str_vector.size):
        result = result + str_vector[i]
    return result


def sel(a, b):
    """Select elements of a at indices b, zero elsewhere."""
    a_b = np.zeros(np.shape(a))
    a_b[b] = a[b]
    return a_b


def init_list_of_objects(size):
    """Create a list of empty lists."""
    return [[] for _ in range(size)]
