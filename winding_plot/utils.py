"""
Utility drawing functions.

Helper functions for annotations, arc arrows, and color-coding.
"""

import matplotlib.pyplot as plt
import numpy as np


def draw_arc_arrow(radius, arc_start, arc_stop, label):
    """
    Draw an arc arrow annotation.

    Parameters
    ----------
    radius : float
        Radius of the arc.
    arc_start : float
        Start angle in degrees.
    arc_stop : float
        Stop angle in degrees.
    label : str
        Label text to place at the midpoint of the arc.
    """
    alpha = np.linspace(arc_start, arc_stop, 100) / 180 * np.pi
    x = radius * np.cos(alpha)
    y = radius * np.sin(alpha)
    plt.plot(x, y, c='k')

    x0 = x[-2]
    y0 = y[-2]
    x1 = x[-1]
    y1 = y[-1]
    plt.arrow(x0, y0, x1 - x0, y1 - y0,
              length_includes_head=True, ec='k', fc='k', width=0.005)

    plt.text(radius * np.cos(np.mean(alpha)), radius * np.sin(np.mean(alpha)),
             label, verticalalignment='center', horizontalalignment='center',
             fontsize=18)
    plt.axis('equal')


def draw_pole_color(n_slots, b0=1, b1=1.2, color=None):
    """
    Color the stator poles alternately.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    b0 : float
        Inner radius.
    b1 : float
        Outer radius.
    color : list of str
        Two colors for alternating poles.
    """
    if color is None:
        color = ['r', 'k']
    for i in range(n_slots):
        a0 = 2 * np.pi / n_slots * i - np.pi / n_slots
        a1 = 2 * np.pi / n_slots * (i + 1) - np.pi / n_slots

        a = np.linspace(a0, a1, 100)
        x = b1 * np.cos(a)
        y = b1 * np.sin(a)
        a_ = np.linspace(a1, a0, 100)
        x_ = b0 * np.cos(a_)
        y_ = b0 * np.sin(a_)

        plt.fill(np.hstack((b0 * np.cos(a0), b1 * np.cos(a0), x, b1 * np.cos(a1), b0 * np.cos(a1), x_)),
                 np.hstack((b0 * np.sin(a0), b1 * np.sin(a0), y, b1 * np.sin(a1), b0 * np.sin(a1), y_)),
                 color=color[np.mod(i, 2)])


def draw_phase_color(n_slots, b0=1, b1=1.2, color=None):
    """
    Color the stator by phase.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    b0 : float
        Inner radius.
    b1 : float
        Outer radius.
    color : list of str
        Colors for each phase.
    """
    if color is None:
        color = ['blue', 'cyan', 'gold']
    for i in range(n_slots):
        a0 = 2 * np.pi / n_slots * i - np.pi / n_slots
        a1 = 2 * np.pi / n_slots * (i + 1) - np.pi / n_slots

        a = np.linspace(a0, a1, 100)
        x = b1 * np.cos(a)
        y = b1 * np.sin(a)
        a_ = np.linspace(a1, a0, 100)
        x_ = b0 * np.cos(a_)
        y_ = b0 * np.sin(a_)

        plt.fill(np.hstack((b0 * np.cos(a0), b1 * np.cos(a0), x, b1 * np.cos(a1), b0 * np.cos(a1), x_)),
                 np.hstack((b0 * np.sin(a0), b1 * np.sin(a0), y, b1 * np.sin(a1), b0 * np.sin(a1), y_)),
                 color=color[np.mod(i, 3)])


def draw_phase_index(n_slots, b=1.8):
    """
    Draw phase labels (A, B, C, ...) at given radius.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    b : float
        Label radius.
    """
    phase_names = ['A', 'C', 'B', 'D', 'E', 'F']
    for i in range(n_slots):
        a = 2 * np.pi / n_slots * i
        x = b * np.cos(a)
        y = b * np.sin(a)
        plt.text(x, y, phase_names[np.mod(i, 3)],
                 horizontalalignment='center', verticalalignment='center')


def draw_pole_index(n_slots, b=1.8):
    """
    Draw pole labels (+/-) at given radius.

    Parameters
    ----------
    n_slots : int
        Number of slots.
    b : float
        Label radius.
    """
    pole_names = ['+', '-']
    for i in range(n_slots):
        a = 2 * np.pi / n_slots * i
        x = b * np.cos(a)
        y = b * np.sin(a)
        plt.text(x, y, pole_names[np.mod(i, 2)],
                 horizontalalignment='center', verticalalignment='center')
