"""
MMF distribution visualization functions.

Star of MMFs plots showing the normalized MMF phasor distribution.
"""

import matplotlib.pyplot as plt
import numpy as np


def draw_star_of_mmfs(phasors, color, line_style='-', show_arrow=False):
    """
    Draw the normalized MMF distribution as a star diagram.

    Parameters
    ----------
    phasors : ndarray
        Complex MMF phasor values.
    color : str
        Matplotlib color string.
    line_style : str
        Line style for the phasors.
    show_arrow : bool
        If True, show arc arrow annotation.
    """
    phasors = phasors / np.amax(np.abs(phasors))
    n_phasors = np.size(phasors, axis=0)

    draw_polar_coordinate_system(np.angle(phasors) / (2 * np.pi / n_phasors))

    for i in range(n_phasors):
        x = (np.abs(phasors[i]) - 0.1) * np.cos(np.angle(phasors[i]))
        y = (np.abs(phasors[i]) - 0.1) * np.sin(np.angle(phasors[i]))
        plt.arrow(0, 0, x, y, head_width=0.05, head_length=0.1,
                  fc=color, ec=color, linestyle=line_style)

    if show_arrow:
        from winding_plot.utils import draw_arc_arrow
        draw_arc_arrow(Radius=1.2, ArcStart=0,
                       ArcStop=180 / np.pi * np.angle(phasors[1]),
                       Label=r'$\gamma\frac{2\pi}{N_s}n$')

    plt.axis('equal')
    plt.axis('off')


def draw_star_of_mmf_and_currents(mmf_phasors, mmf_color, mmf_style,
                                    current_phasors, current_color, current_style,
                                    n_phasors):
    """
    Draw both MMF distribution and current system on the same polar plot.

    Parameters
    ----------
    mmf_phasors : ndarray
        Complex MMF phasor values.
    mmf_color : str
        Color for MMF phasors.
    mmf_style : str
        Line style for MMF phasors.
    current_phasors : ndarray
        Complex current phasor values.
    current_color : str
        Color for current phasors.
    current_style : str
        Line style for current phasors.
    n_phasors : int
        Number of phasors.
    """
    draw_star_of_mmfs(mmf_phasors, mmf_color, mmf_style)

    for i in range(n_phasors):
        x = np.cos(np.angle(current_phasors[i]))
        y = np.sin(np.angle(current_phasors[i]))
        plt.plot([0, x], [0, y], color=current_color, linestyle=current_style)


def draw_polar_coordinate_system(harmonic_vector):
    """Draw a polar coordinate system."""
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
