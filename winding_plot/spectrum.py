"""
Spectrum visualization functions.

Winding factor harmonic spectrum plots in polar and bar chart form.
"""

import matplotlib.pyplot as plt
import numpy as np


def show_winding_spectrum(winding_spectrum):
    """
    Bar chart of the winding factor harmonic spectrum.

    Parameters
    ----------
    winding_spectrum : ndarray
        Complex winding factor spectrum.
    """
    n_slots = np.size(winding_spectrum, axis=0)
    if bool(n_slots % 2):
        harmonic_neg_limit = -(n_slots + 1) / 2 + 1
        harmonic_pos_limit = (n_slots - 1) / 2
    else:
        harmonic_neg_limit = -n_slots / 2 + 1
        harmonic_pos_limit = n_slots / 2

    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_slots)
    h_plot = np.hstack([harmonic_vector, harmonic_vector - n_slots, harmonic_vector + n_slots])
    s_plot = np.hstack([winding_spectrum, winding_spectrum, winding_spectrum])

    plt.bar(np.abs(h_plot)[h_plot < 0], np.abs(s_plot)[h_plot < 0],
            color='r', align='center')
    plt.bar(np.abs(h_plot)[h_plot > 0], np.abs(s_plot)[h_plot > 0],
            color='k', align='center')
    plt.xlabel('Harmonic Order')
    plt.ylabel('Winding Factor')
    plt.tight_layout()
    plt.grid(True)
    plt.ylim(0, 1)


def draw_polar_coordinate_system(harmonic_vector):
    """
    Draw a polar coordinate system for the star of slots diagram.

    Parameters
    ----------
    harmonic_vector : ndarray
        Harmonic order vector.
    """
    n_harmonics = np.size(harmonic_vector)
    alpha = np.linspace(0, 2 * np.pi, 100)
    for r in np.linspace(0, 1, 6):
        plt.plot(r * np.cos(alpha), r * np.sin(alpha), linestyle=':', color='black')
    plt.plot(np.cos(alpha), np.sin(alpha), 'black')

    for i in range(n_harmonics):
        x = np.cos(2 * np.pi / n_harmonics * harmonic_vector[i])
        y = np.sin(2 * np.pi / n_harmonics * harmonic_vector[i])
        plt.plot([0, x], [0, y], linestyle=':', color='black')
        plt.text(1.1 * x, 1.1 * y, "%i" % i,
                 horizontalalignment='center', verticalalignment='center')


def draw_star_of_spectrums(winding_factor_spectrum, color):
    """
    Draw the winding factor harmonic spectrum as a star (polar) diagram.

    Parameters
    ----------
    winding_factor_spectrum : ndarray
        Complex winding factor spectrum.
    color : str
        Matplotlib color string for the spectrum phasors.
    """
    alpha = np.linspace(0, 2 * np.pi, 100)
    for r in np.linspace(0, 1, 6):
        plt.plot(r * np.cos(alpha), r * np.sin(alpha), linestyle=':', color='black')
    plt.plot(np.cos(alpha), np.sin(alpha), 'black')

    n_harmonics = np.size(winding_factor_spectrum, axis=0)
    if bool(n_harmonics % 2):
        harmonic_neg_limit = -(n_harmonics + 1) / 2 + 1
        harmonic_pos_limit = (n_harmonics - 1) / 2
    else:
        harmonic_neg_limit = -n_harmonics / 2 + 1
        harmonic_pos_limit = n_harmonics / 2
    harmonic_vector = np.linspace(harmonic_neg_limit, harmonic_pos_limit, n_harmonics)

    for i in range(n_harmonics):
        x = np.cos(2 * np.pi / n_harmonics * harmonic_vector[i])
        y = np.sin(2 * np.pi / n_harmonics * harmonic_vector[i])
        plt.plot([0, x], [0, y], linestyle=':', color='black')
        plt.text(1.1 * x, 1.1 * y, "%i" % harmonic_vector[i],
                 horizontalalignment='center', verticalalignment='center')

    # Spectrum phasors
    for i in range(n_harmonics):
        phasor = np.abs(winding_factor_spectrum[i]) * np.exp(1j * 2 * np.pi)
        x = np.real(phasor)
        y = np.imag(phasor)
        plt.plot([0, x], [0, y], color)

    plt.axis('equal')
    plt.axis('off')
    plt.subplots_adjust(left=0.0, right=1., top=1., bottom=0.)
