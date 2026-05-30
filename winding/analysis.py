"""
Winding topology analysis functions.

Functions for calculating winding factor harmonic spectra, MMF distributions,
and the transformation between space and spectrum domains.

Author: Mang Cai (original CaisModule.py, 2016)
Refactored: 2026
"""

import warnings

import numpy as np
from numpy import linalg as LA

from winding.models import WindingSpectrum, MMF


# ============================================================================
# Internal helpers (shared across analysis functions)
# ============================================================================

def _build_harmonic_vector(n_slots):
    """Build the harmonic order vector for a given number of slots.

    For even N:  [-N/2+1, -N/2+2, ..., 0, ..., N/2]
    For odd N:   [-(N+1)/2+1, ..., 0, ..., (N-1)/2]

    Parameters
    ----------
    n_slots : int
        Number of slots.

    Returns
    -------
    ndarray
        Harmonic order vector of length n_slots.
    """
    if n_slots % 2:
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2
    return np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots)


def _build_transformation_matrix(n_slots, position_start=1, endpoint=True):
    """Build the DFT-like transformation matrix for winding factor calculation.

    The transformation maps between the spatial conductor distribution
    and the winding factor harmonic spectrum domain.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    position_start : int
        Starting index for slot positions (1 for spectrum, 0 for MMF).
    endpoint : bool
        Whether to include the endpoint in the position vector.

    Returns
    -------
    ndarray
        Complex transformation matrix of shape (n_slots, n_slots).
    harmonic_vector : ndarray
        Harmonic order vector of length n_slots.
    """
    position_vector = np.linspace(position_start, n_slots, n_slots, endpoint=endpoint)
    harmonic_vector = _build_harmonic_vector(n_slots)
    position_matrix, harmonic_matrix = np.meshgrid(position_vector, harmonic_vector)
    transformation_matrix = np.exp(
        -1j * harmonic_matrix * 2 * np.pi / n_slots * position_matrix)
    return transformation_matrix, harmonic_vector


# ============================================================================
# Core spectrum calculation
# ============================================================================

def winding_topology_to_spectrum(winding_topology, current_phase_vector):
    """Calculate the winding factor harmonic spectrum from a winding topology.

    Parameters
    ----------
    winding_topology : ndarray
        Conductor distribution matrix of shape (n_slots, n_phases).
    current_phase_vector : ndarray
        Complex vector of phase currents.

    Returns
    -------
    ndarray
        Complex winding factor harmonic spectrum of shape (n_slots,).
    """
    winding_topology = winding_topology / np.sum(np.abs(winding_topology))
    n_slots = np.size(winding_topology, axis=0)

    transformation_matrix, _ = _build_transformation_matrix(n_slots)
    return transformation_matrix.dot(winding_topology.dot(current_phase_vector))


def winding_topology_to_spectrum_with_harmonics(winding_topology, current_phase_vector):
    """Like winding_topology_to_spectrum but also returns the harmonic order vector.

    Parameters
    ----------
    winding_topology : ndarray
        Conductor distribution matrix of shape (n_slots, n_phases).
    current_phase_vector : ndarray
        Complex vector of phase currents.

    Returns
    -------
    spectrum : ndarray
        Complex winding factor harmonic spectrum.
    harmonic_vector : ndarray
        Harmonic order vector of length n_slots.
    """
    spectrum = winding_topology_to_spectrum(winding_topology, current_phase_vector)
    n_slots = np.size(winding_topology, axis=0)
    _, harmonic_vector = _build_transformation_matrix(n_slots)
    return spectrum, harmonic_vector


# ============================================================================
# Ideal spectrum and MMF
# ============================================================================

def get_ideal_winding_spectrum(n_slots, working_harmonic):
    """Create an ideal winding spectrum with only the working harmonic present.

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
    """Calculate the normalized MMF distribution from a winding spectrum.

    The MMF distribution is obtained by solving the linear system
    defined by the transformation matrix: T @ mmf = spectrum.

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

    transformation_matrix, _ = _build_transformation_matrix(
        n_slots, position_start=0, endpoint=False)
    normalized_mmf = LA.solve(transformation_matrix, winding_spectrum)

    mmf_obj.transformation_matrix = transformation_matrix
    mmf_obj.distribution = normalized_mmf
    return mmf_obj


def get_normalized_mmf_vector(winding_spectrum):
    """Legacy-style: return a list with [transformation_matrix, normalized_mmf_vector].

    .. deprecated::
        Use get_mmf() instead, which returns an MMF object.

    Parameters
    ----------
    winding_spectrum : list
        List where first element is the spectrum distribution array.

    Returns
    -------
    list
        [transformation_matrix, normalized_mmf_vector]
    """
    warnings.warn(
        "get_normalized_mmf_vector is deprecated, use get_mmf() instead.",
        DeprecationWarning, stacklevel=2)

    spectrum = winding_spectrum[0]
    n_slots = np.size(spectrum, axis=0)

    transformation_matrix, _ = _build_transformation_matrix(
        n_slots, position_start=0, endpoint=False)
    normalized_mmf = LA.solve(transformation_matrix, spectrum)
    winding_spectrum.append([transformation_matrix, normalized_mmf])
    return winding_spectrum
