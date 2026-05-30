"""
Winding topology analysis functions.

Functions for calculating winding factor harmonic spectra, MMF distributions,
and the transformation between space and spectrum domains.

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import numpy as np
from numpy import linalg as LA
from winding.models import WindingSpectrum, MMF


def winding_topology_to_spectrum(winding_topology, current_phase_vector):
    """
    Calculate the winding factor harmonic spectrum from a winding topology.

    Parameters
    ----------
    winding_topology : ndarray
        Conductor distribution matrix of shape (n_slots, n_phases).
    current_phase_vector : ndarray
        Complex vector of phase currents.

    Returns
    -------
    ndarray
        Complex winding factor harmonic spectrum.
    """
    # Normalize (conductor-number-independent winding topology)
    winding_topology = winding_topology / np.sum(np.abs(winding_topology))

    n_slots = np.size(winding_topology, axis=0)
    position_vector = np.linspace(1, n_slots, n_slots)

    # Harmonic order vector
    if bool(n_slots % 2):
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2
    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots)

    # Transformation matrix (DFT-like)
    position_matrix, harmonic_matrix = np.meshgrid(position_vector, harmonic_vector)
    transformation_matrix = np.exp(-1j * harmonic_matrix * 2 * np.pi / n_slots * position_matrix)

    return transformation_matrix.dot(winding_topology.dot(current_phase_vector))


def winding_topology_to_spectrum_with_harmonics(winding_topology, current_phase_vector):
    """Like winding_topology_to_spectrum but also returns the harmonic order vector."""
    spectrum = winding_topology_to_spectrum(winding_topology, current_phase_vector)
    n_slots = np.size(winding_topology, axis=0)
    if bool(n_slots % 2):
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2
    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots)
    return spectrum, harmonic_vector


def get_ideal_winding_spectrum(n_slots, working_harmonic):
    """
    Create an ideal winding spectrum with only the working harmonic present.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    working_harmonic : int
        The desired working harmonic order.

    Returns
    -------
    WindingSpectrum
        Object containing the ideal spectrum distribution.
    """
    return WindingSpectrum(n_slots, working_harmonic, type_='Ideal')


def get_mmf(winding_spectrum_obj):
    """
    Calculate the normalized MMF distribution from a winding spectrum.

    Parameters
    ----------
    winding_spectrum_obj : WindingSpectrum
        Object containing the winding factor harmonic spectrum.

    Returns
    -------
    MMF
        Object containing the normalized MMF distribution.
    """
    mmf_obj = MMF(winding_spectrum_obj)
    winding_spectrum = winding_spectrum_obj.distribution

    n_slots = np.size(winding_spectrum, axis=0)
    position_vector = np.linspace(0, n_slots, n_slots, endpoint=False)

    if bool(n_slots % 2):
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2
    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots)

    position_matrix, harmonic_matrix = np.meshgrid(position_vector, harmonic_vector)
    transformation_matrix = np.exp(-1j * harmonic_matrix * 2 * np.pi / n_slots * position_matrix)

    normalized_mmf = LA.solve(transformation_matrix, winding_spectrum)

    mmf_obj.transformation_matrix = transformation_matrix
    mmf_obj.distribution = normalized_mmf
    return mmf_obj


def get_normalized_mmf_vector(winding_spectrum):
    """
    Legacy-style: return a list with [transformation_matrix, normalized_mmf_vector].

    Parameters
    ----------
    winding_spectrum : list
        List where first element is the spectrum distribution array.

    Returns
    -------
    list
        [transformation_matrix, normalized_mmf_vector]
    """
    spectrum = winding_spectrum[0]
    n_slots = np.size(spectrum, axis=0)
    position_vector = np.linspace(0, n_slots, n_slots, endpoint=False)

    if bool(n_slots % 2):
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2
    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots)

    position_matrix, harmonic_matrix = np.meshgrid(position_vector, harmonic_vector)
    transformation_matrix = np.exp(-1j * harmonic_matrix * 2 * np.pi / n_slots * position_matrix)

    normalized_mmf = LA.solve(transformation_matrix, spectrum)
    winding_spectrum.append([transformation_matrix, normalized_mmf])
    return winding_spectrum
