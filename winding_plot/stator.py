"""
Stator cross-section drawing functions.

Functions for drawing the stator teeth, slots, and conductors.
"""

import matplotlib.pyplot as plt
import numpy as np


def draw_stator2(n_slots, tooth_width_ratio=0.4, rotation_angle=0):
    """
    Draw a stator cross-section with teeth and slots.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    tooth_width_ratio : float
        Ratio of tooth width to slot pitch.
    rotation_angle : float
        Initial rotation angle in degrees.

    Returns
    -------
    tooth_outer_radius : float
        Outer radius of the teeth.
    tooth_width : float
        Width of each tooth.
    tooth_height : float
        Height (radial depth) of each tooth.
    """
    tooth_outer_radius = 1.2
    tooth_inner_radius = 0.6
    tooth_height = tooth_outer_radius - tooth_inner_radius
    tooth_width = tooth_width_ratio * 2 * np.pi / n_slots * tooth_outer_radius

    rot = rotation_angle * np.pi / 180

    for n in range(n_slots):
        a0 = 2 * np.pi / n_slots * n - np.pi / n_slots + rot
        a1 = 2 * np.pi / n_slots * (n + 1) - np.pi / n_slots + rot

        # Slot area (fill between teeth)
        x_fill = [tooth_inner_radius * np.cos(a0),
                  tooth_outer_radius * np.cos(a0),
                  tooth_outer_radius * np.cos(a1),
                  tooth_inner_radius * np.cos(a1)]
        y_fill = [tooth_inner_radius * np.sin(a0),
                  tooth_outer_radius * np.sin(a0),
                  tooth_outer_radius * np.sin(a1),
                  tooth_inner_radius * np.sin(a1)]

        if n % 2 == 0:
            plt.fill(x_fill, y_fill, color='lightgray')
        else:
            plt.fill(x_fill, y_fill, color='white')

        # Slot opening
        a_mid = (a0 + a1) / 2
        so_half = np.pi / n_slots * (1 - tooth_width_ratio) / 2
        so_x = [tooth_outer_radius * np.cos(a_mid - so_half),
                tooth_outer_radius * 1.05 * np.cos(a_mid - so_half),
                tooth_outer_radius * 1.05 * np.cos(a_mid + so_half),
                tooth_outer_radius * np.cos(a_mid + so_half)]
        so_y = [tooth_outer_radius * np.sin(a_mid - so_half),
                tooth_outer_radius * 1.05 * np.sin(a_mid - so_half),
                tooth_outer_radius * 1.05 * np.sin(a_mid + so_half),
                tooth_outer_radius * np.sin(a_mid + so_half)]
        plt.fill(so_x, so_y, color='white')

    return tooth_outer_radius, tooth_width, tooth_height


def go_conductor(ox, oy, or_, rotation_angle, color):
    """
    Draw a 'going' conductor (cross-section with dot).

    Parameters
    ----------
    ox : float
        Radial position.
    oy : float
        Tangential position.
    or_ : float
        Conductor radius.
    rotation_angle : float
        Rotation angle in degrees.
    color : str
        Fill color.
    """
    x, y = rotation(np.atleast_1d(ox), np.atleast_1d(oy), rotation_angle)
    alpha = np.linspace(0, 2 * np.pi, 50)
    circle = plt.Circle((x[0], y[0]), or_, color=color, ec='black', lw=0.5)
    plt.gca().add_patch(circle)
    # Dot in center
    plt.plot(x[0], y[0], 'o', color='black', markersize=2)


def return_conductor(ox, oy, or_, rotation_angle, color):
    """
    Draw a 'returning' conductor (cross-section with cross).

    Parameters
    ----------
    ox : float
        Radial position.
    oy : float
        Tangential position.
    or_ : float
        Conductor radius.
    rotation_angle : float
        Rotation angle in degrees.
    color : str
        Fill color.
    """
    x, y = rotation(np.atleast_1d(ox), np.atleast_1d(oy), rotation_angle)
    alpha = np.linspace(0, 2 * np.pi, 50)
    circle = plt.Circle((x[0], y[0]), or_, color=color, ec='black', lw=0.5)
    plt.gca().add_patch(circle)
    # Cross in center
    plt.plot(x[0], y[0], 'x', color='black', markersize=4)


def rotation(x, y, rotation_angle):
    """
    Rotate coordinates by a given angle.

    Parameters
    ----------
    x : ndarray
        x-coordinates.
    y : ndarray
        y-coordinates.
    rotation_angle : float
        Rotation angle in degrees.

    Returns
    -------
    xr : ndarray
        Rotated x-coordinates.
    yr : ndarray
        Rotated y-coordinates.
    """
    rad = rotation_angle * np.pi / 180
    xr = x * np.cos(rad) - y * np.sin(rad)
    yr = x * np.sin(rad) + y * np.cos(rad)
    return xr, yr
