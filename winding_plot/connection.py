"""
Connection matrix visualization functions.

Functions for drawing the conductor distribution matrix, conductor plan,
and coil group diagrams.
"""

import matplotlib.pyplot as plt
import numpy as np


def draw_connection_matrix(connection_matrix, multi_phase_current_system,
                            color=None, with_mmf=1, with_text=None, alpha=None):
    """
    Draw the normalized conductor distribution matrix as a star diagram.

    Parameters
    ----------
    connection_matrix : ndarray
        Connection matrix of shape (n_slots, n_phases).
    multi_phase_current_system : ndarray
        Complex multi-phase current system.
    color : list of str or None
        Colors for each phase.
    with_mmf : int
        If 1, overlay the MMF distribution.
    with_text : list of int or None
        If 1 for a phase, show phase label.
    alpha : list of float or None
        Alpha values for each phase.
    """
    n_slots = np.size(connection_matrix, axis=0)
    n_phases = np.size(connection_matrix, axis=1)

    if color is None:
        color = ['b', 'b', 'b']
    if with_text is None:
        with_text = [1, 1, 1]
    if alpha is None:
        alpha = [1.0] * n_phases

    conn_matrix = connection_matrix * n_slots
    phase_names = [['A', 'B', 'C', 'D', 'E', 'F'],
                    [],
                    ['A', 'B', 'C', 'D', 'E', 'F']]

    for i in range(n_slots):
        idx_phase = np.argsort(np.abs(conn_matrix[i, :]))[::-1]
        sign_phase = np.int64(np.sign(conn_matrix[i, idx_phase]))
        phasor = conn_matrix[i, idx_phase] * multi_phase_current_system[idx_phase]
        sign_phase = sign_phase[np.nonzero(phasor)]
        idx_phase = idx_phase[np.nonzero(phasor)]
        phasor = phasor[np.nonzero(phasor)]

        if phasor.size == 0:
            continue

        # First conductor
        x0 = (np.abs(phasor[0]) - 0.1) * np.cos(np.angle(phasor[0]))
        y0 = (np.abs(phasor[0]) - 0.1) * np.sin(np.angle(phasor[0]))
        plt.arrow(0, 0, x0, y0, head_width=0.05, head_length=0.1,
                  fc=color[idx_phase[0]], ec=color[idx_phase[0]],
                  alpha=alpha[idx_phase[0]])

        if with_text[idx_phase[0]] == 1:
            x_t = (np.abs(phasor[0])) * np.cos(np.angle(phasor[0]))
            y_t = (np.abs(phasor[0])) * np.sin(np.angle(phasor[0]))
            x_off = 0.2 * np.cos(np.angle(phasor[0]))
            y_off = 0.2 * np.sin(np.angle(phasor[0]))
            plt.text(x_t - x_off, y_t - y_off,
                     phase_names[sign_phase[0] + 1][idx_phase[0]],
                     horizontalalignment='center', verticalalignment='center')

        # Second conductor (if exists)
        if phasor.size >= 2:
            x1 = (np.abs(phasor[1]) - 0.1) * np.cos(np.angle(phasor[1]))
            y1 = (np.abs(phasor[1]) - 0.1) * np.sin(np.angle(phasor[1]))
            plt.arrow(x0, y0, x1, y1, head_width=0.05, head_length=0.1,
                      fc=color[idx_phase[1]], ec=color[idx_phase[1]],
                      alpha=alpha[idx_phase[1]])

            if with_text[idx_phase[1]] == 1:
                x_t = (np.abs(phasor[1])) * np.cos(np.angle(phasor[1]))
                y_t = (np.abs(phasor[1])) * np.sin(np.angle(phasor[1]))
                plt.text((x0 + x_t + x0) / 2, (y0 + y_t + y0) / 2,
                         phase_names[sign_phase[1] + 1][idx_phase[1]],
                         horizontalalignment='center', verticalalignment='center')

    if with_mmf:
        mmf_distribution = conn_matrix.dot(multi_phase_current_system)
        from winding_plot.mmf import draw_star_of_mmfs
        draw_star_of_mmfs(mmf_distribution, 'r', '--')

    alpha_circle = np.linspace(0, 2 * np.pi, 100)
    plt.fill(0.05 * np.cos(alpha_circle), 0.05 * np.sin(alpha_circle), 'black')

    if with_mmf == 0:
        plt.plot(1 * np.cos(alpha_circle), 1 * np.sin(alpha_circle), 'w')

    plt.axis('equal')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axis('off')


def draw_conductor_plan_of_connection_matrix(connection_matrix,
                                              tooth_width_ratio=0.4, or_=0.15,
                                              color=None, flag_of_show=None,
                                              n_conductors_per_slot=100):
    """
    Draw the conductor placement plan for a given connection matrix.

    Parameters
    ----------
    connection_matrix : ndarray
        Connection matrix of shape (n_slots, n_phases).
    tooth_width_ratio : float
        Ratio of tooth width to slot pitch.
    or_ : float
        Conductor radius.
    color : list of str or None
        Colors for each phase.
    flag_of_show : list of int or None
        Which phases to show.
    n_conductors_per_slot : int
        Scaling factor for conductor count.
    """
    from winding_plot.stator import draw_stator2, go_conductor, return_conductor, rotation

    N = np.size(connection_matrix, axis=0)
    if color is None:
        color = ['lime', 'gold', 'b']
    if flag_of_show is None:
        flag_of_show = [1, 1, 1]

    conn_matrix = connection_matrix * N * n_conductors_per_slot
    tooth_outer_radius, tooth_width, tooth_height = draw_stator2(
        N, tooth_width_ratio, rotation_angle=180.0 / N)

    for n in range(N):
        rotation_angle = np.rad2deg(2 * np.pi / N * n)

        # Negative winding direction first
        idx_phase = np.argsort(conn_matrix[n, :])
        conn_vec = conn_matrix[n, idx_phase]
        idx_phase = idx_phase[np.nonzero(conn_vec)]
        conn_vec = conn_vec[np.nonzero(conn_vec)]

        if conn_vec.size == 0:
            continue

        if conn_vec.size == 1:
            conn_vec = conn_vec / 2
            conn_vec = np.append(conn_vec, conn_vec)
            idx_phase = np.append(idx_phase, idx_phase)

        # First winding layer
        ox1 = tooth_outer_radius - or_
        oy = 0.0

        if flag_of_show[idx_phase[0]] == 1:
            if np.sign(conn_vec[0]) == 1:
                go_conductor(ox1, oy, or_, rotation_angle, color[idx_phase[0]])
            elif np.sign(conn_vec[0]) == -1:
                return_conductor(ox1, oy, or_, rotation_angle, color[idx_phase[0]])

            tx = np.atleast_1d(ox1) + 2.5 * or_
            ty = np.atleast_1d(oy)
            tx, ty = rotation(tx, ty, rotation_angle)
            plt.text(tx, ty, "%i" % np.rint(conn_vec[0]),
                     horizontalalignment='center', verticalalignment='center')

        # Second winding layer
        if flag_of_show[idx_phase[1]] == 1:
            ox2 = ox1 - 2 * or_ * 1.2
            oy = 0.0
            if np.sign(conn_vec[1]) == 1:
                go_conductor(ox2, oy, or_, rotation_angle, color[idx_phase[1]])
            elif np.sign(conn_vec[1]) == -1:
                return_conductor(ox2, oy, or_, rotation_angle, color[idx_phase[1]])

            tx = np.atleast_1d(ox2) - 3. * or_
            ty = np.atleast_1d(oy)
            tx, ty = rotation(tx, ty, rotation_angle)
            plt.text(tx, ty, "%i" % np.rint(conn_vec[1]),
                     horizontalalignment='center', verticalalignment='center')

    plt.axis('equal')
    plt.axis('off')


def draw_conductor_plan_of_coil_group(connection_vector, or_=0.15):
    """
    Draw the conductor plan for a single coil group.

    Parameters
    ----------
    connection_vector : ndarray
        Single-phase connection vector.
    or_ : float
        Conductor radius.
    """
    from winding_plot.stator import draw_stator2, go_conductor, return_conductor, rotation

    N = np.size(connection_vector, axis=0)
    conn_vec = connection_vector * N * 100
    tooth_outer_radius, _, _ = draw_stator2(N, 0.4, rotation_angle=180.0 / N)

    for n in range(N):
        rotation_angle = np.rad2deg(2 * np.pi / N * n)
        if conn_vec[n] > 0:
            go_conductor(tooth_outer_radius - or_, 0.0, or_, rotation_angle, 'lime')
        elif conn_vec[n] < 0:
            return_conductor(tooth_outer_radius - or_, 0.0, or_, rotation_angle, 'lime')

        tx = np.atleast_1d(tooth_outer_radius - or_) + 2.5 * or_
        ty = np.atleast_1d(0.0)
        tx, ty = rotation(tx, ty, rotation_angle)
        plt.text(tx, ty, "%i" % np.rint(conn_vec[n]),
                 horizontalalignment='center', verticalalignment='center')

    plt.axis('equal')
    plt.axis('off')


def draw_connection(connection_vector, or_=0.13, posi_flag=0,
                    draw_connection=1, color='b'):
    """
    Draw a single connection (coil side) on the stator cross-section.

    Parameters
    ----------
    connection_vector : ndarray
        Connection vector for one coil.
    or_ : float
        Conductor radius.
    posi_flag : int
        Position flag: 0=upper, 1=middle, 2=lower.
    draw_connection : int
        If 1, draw the conductor.
    color : str
        Conductor color.

    Returns
    -------
    oxm : float
        x-coordinate of the conductor midpoint.
    oym : float
        y-coordinate of the conductor midpoint.
    """
    from winding_plot.stator import go_conductor, return_conductor, rotation

    N = np.size(connection_vector, axis=0)
    tooth_outer_radius = 1.2
    positions = [tooth_outer_radius - or_,
                 tooth_outer_radius - 2 * or_ * 1.2,
                 tooth_outer_radius - 3 * or_ * 1.2]

    ox = positions[posi_flag]
    oy = 0.0

    oxm = np.zeros(N)
    oym = np.zeros(N)

    for n in range(N):
        rotation_angle = np.rad2deg(2 * np.pi / N * n)
        if draw_connection:
            if connection_vector[n] > 0:
                go_conductor(ox, oy, or_, rotation_angle, color)
            elif connection_vector[n] < 0:
                return_conductor(ox, oy, or_, rotation_angle, color)
        oxm[n], oym[n] = rotation(np.atleast_1d(ox), np.atleast_1d(oy), rotation_angle)

    return oxm, oym


def draw_number_of_turn(oxm, oym, or_=0.13, posi_text=0, n_turn=1):
    """
    Annotate the number of turns on a conductor.

    Parameters
    ----------
    oxm : ndarray
        x-coordinates of conductor midpoints.
    oym : ndarray
        y-coordinates of conductor midpoints.
    or_ : float
        Conductor radius.
    posi_text : int
        Text position offset index.
    n_turn : int
        Number of turns to display.
    """
    offsets = [2.5, 3.5, 4.5]
    for n in range(oxm.size):
        plt.text(oxm[n] + offsets[posi_text] * or_,
                 oym[n] + offsets[posi_text] * or_,
                 "%i" % n_turn,
                 horizontalalignment='center', verticalalignment='center')
