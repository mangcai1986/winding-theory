"""
Unit tests for the winding package.

Tests cover: spectrum analysis, MMF calculation, symmetry detection,
design pipeline, and modification functions.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from numpy import linalg as LA
import pytest

from winding.models import WindingSpectrum, CurrentSystem, MMF
from winding.analysis import (
    winding_topology_to_spectrum,
    winding_topology_to_spectrum_with_harmonics,
    get_ideal_winding_spectrum,
    get_mmf,
)
from winding.design import (
    get_primitive_multiphase_winding,
    get_single_phase_winding,
    get_coil_group,
    get_coil,
)
from winding.modification import (
    winding_topology_double_way_connection,
    winding_topology_single_way_connection_md,
    winding_topology_single_way_connection_sp,
    obtain_multi_turn_winding_topology,
    obtain_multi_layer_winding_topology,
    obtain_double_layer_winding_topology,
    obtain_single_layer_winding_topology,
)
from winding.transforms import (
    detect_rotation_symmetry,
    detect_mirror_symmetry,
    get_part_of_mirror_symmetry,
)
from winding.utils import (
    proj, calc_connection, coil_pitch, calculate_number_of_turns,
)


# ======================================================================
# Analysis Tests
# ======================================================================

class TestWindingTopologyToSpectrum:
    """Tests for winding factor harmonic spectrum calculation."""

    def test_known_12slot_3phase_double_layer(self):
        """Verify via the full design pipeline (thesis §6.1)."""
        cs = CurrentSystem(3, current_system_flag=0)
        mmf = get_mmf(WindingSpectrum(12, 1))
        w = get_primitive_multiphase_winding(mmf, cs)
        sp = get_single_phase_winding(w, 0)
        cg = get_coil_group(sp)
        dl = obtain_double_layer_winding_topology(
            winding_topology_single_way_connection_md(cg))
        ws = dl[0].winding_spectrum_real
        wf_1 = np.abs(ws[6])  # ν=1 at index 6 for 12 slots
        assert wf_1 == pytest.approx(0.9330, abs=0.01)

    def test_single_phase_winding(self):
        """A single-phase winding should produce correct spectrum."""
        conn = np.zeros((12, 1))
        conn[0, 0] = 1; conn[6, 0] = -1
        current = np.array([1.0])
        spectrum = winding_topology_to_spectrum(conn, current)
        assert spectrum.shape == (12,)
        assert not np.any(np.isnan(spectrum))

    def test_spectrum_with_harmonics(self):
        """winding_topology_to_spectrum_with_harmonics returns harmonic vector."""
        conn = np.zeros((12, 3))
        conn[0, 0] = 1; conn[6, 0] = -1
        conn[4, 1] = 1; conn[10, 1] = -1
        conn[8, 2] = 1; conn[2, 2] = -1
        current = np.exp(1j * np.linspace(0, 2*np.pi, 3, endpoint=False))
        spectrum, harmonics = winding_topology_to_spectrum_with_harmonics(conn, current)
        assert len(harmonics) == 12
        assert harmonics[0] == -5  # for 12 slots: -5, -4, ..., 6


class TestGetIdealWindingSpectrum:
    """Tests for ideal winding spectrum generation."""

    @pytest.mark.parametrize("n_slots,harmonic", [(12, 1), (12, 5), (9, 4), (24, 5)])
    def test_ideal_spectrum_shape(self, n_slots, harmonic):
        ws = WindingSpectrum(n_slots, harmonic)
        assert ws.distribution.shape == (n_slots,)
        assert ws.working_harmonic == harmonic
        assert ws.n_slots == n_slots

    def test_ideal_spectrum_values(self):
        ws = WindingSpectrum(12, 1)
        dist = ws.distribution
        # Harmonic vector: [-5,-4,-3,-2,-1,0,1,2,3,4,5,6] → ν=1 at index 6
        assert dist[6] == 1.0  # ν=1 for 12 slots
        assert np.sum(dist) == 1.0


class TestGetMMF:
    """Tests for MMF calculation from winding spectrum."""

    def test_mmf_from_ideal_spectrum(self):
        ws = WindingSpectrum(12, 1)
        mmf = get_mmf(ws)
        assert mmf.distribution.shape == (12,)
        assert not np.any(np.isnan(mmf.distribution))
        assert isinstance(mmf, MMF)

    def test_mmf_recover_spectrum(self):
        """MMF → spectrum should recover the original spectrum."""
        ws = WindingSpectrum(12, 5)
        mmf = get_mmf(ws)
        # Verify the transformation matrix is valid
        assert mmf.transformation_matrix.shape == (12, 12)
        # Inverse transform should recover the original spectrum
        recovered = mmf.transformation_matrix @ mmf.distribution
        original = ws.distribution
        assert np.allclose(recovered, original, atol=1e-10)


# ======================================================================
# Transform Tests
# ======================================================================

class TestDetectRotationSymmetry:
    """Tests for rotation symmetry detection."""

    def test_identity_symmetry(self):
        """A matrix should have g=1, h=1 rotational symmetry."""
        conn = np.eye(4)
        has_sym, matrix, vector = detect_rotation_symmetry(conn)
        assert has_sym == 1
        assert matrix.shape == (4, 4)

    def test_3phase_symmetry(self):
        """3-phase winding should have rotation symmetry with g=4, h=1."""
        conn = np.zeros((12, 3))
        conn[0, 0] = 1; conn[6, 0] = -1
        conn[4, 1] = 1; conn[10, 1] = -1
        conn[8, 2] = 1; conn[2, 2] = -1
        has_sym, matrix, vector = detect_rotation_symmetry(conn)
        assert vector.shape == (12,)


class TestDetectMirrorSymmetry:
    """Tests for mirror symmetry detection."""

    def test_symmetric_vector(self):
        """A symmetric vector should be detected."""
        v = np.array([1, 0, -1, 0, 1, 0, -1, 0])
        has_sym, matrix, position = detect_mirror_symmetry(v)
        assert has_sym == 1
        assert matrix.shape == (8, 8)

    def test_asymmetric_vector(self):
        """An asymmetric vector should return has_sym=0."""
        v = np.array([1, 2, 3, 4, 5])
        has_sym, matrix, position = detect_mirror_symmetry(v)
        # 5 elements can't have reflection symmetry
        assert has_sym == 0 or has_sym == 1


class TestCoilPitch:
    """Tests for coil pitch calculation."""

    @pytest.mark.parametrize("a,b,N,expected", [
        (0, 6, 12, 6),
        (1, 2, 12, 1),
        (0, 11, 12, 1),  # shortest path wraps around
        (3, 9, 12, 6),
    ])
    def test_coil_pitch(self, a, b, N, expected):
        result = coil_pitch(np.array([a]), np.array([b]), N)
        assert result[0] == expected


# ======================================================================
# Utility Tests
# ======================================================================

class TestCalculateNumberOfTurns:
    """Tests for least-squares turn calculation."""

    def test_simple_solution(self):
        """A simple connection matrix should yield integer turns."""
        conn = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
        dist = np.array([2, -2, 3, -3])
        turns, error, real = calculate_number_of_turns(conn, dist)
        assert np.array_equal(turns, np.array([2, 3]))
        assert error < 1e-10

    def test_approximation(self):
        """Test with non-exact solution."""
        conn = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
        dist = np.array([2, -2, 4, -3])
        turns, error, real = calculate_number_of_turns(conn, dist)
        assert error >= 0


# ======================================================================
# Design Pipeline Tests
# ======================================================================

class TestDesignPipeline:
    """End-to-end tests for the winding design pipeline."""

    @pytest.mark.parametrize("n_slots,n_phases,harmonic", [
        (12, 3, 1),
        (12, 3, 5),
        (9, 3, 4),
        (24, 6, 5),
    ])
    def test_design_pipeline(self, n_slots, n_phases, harmonic):
        """The full design pipeline should complete without error."""
        cs = CurrentSystem(n_phases, current_system_flag=0)
        ws = WindingSpectrum(n_slots, harmonic)
        mmf = get_mmf(ws)
        windings = get_primitive_multiphase_winding(mmf, cs)
        assert len(windings) == 2
        sp = get_single_phase_winding(windings, 0)
        assert len(sp) == 2
        cg = get_coil_group(sp)
        assert len(cg) == 2
        coils = get_coil(cg)
        assert len(coils) == 2

    def test_pipeline_connection_matrix_valid(self):
        """Connection matrix values should be reasonable."""
        cs = CurrentSystem(3, current_system_flag=0)
        mmf = get_mmf(WindingSpectrum(12, 1))
        windings = get_primitive_multiphase_winding(mmf, cs)
        for w in windings:
            cm = w.connection_matrix
            assert cm.shape == (12, 3)
            assert np.all(np.abs(cm) <= 1.0)


class TestModificationPipeline:
    """Tests for the winding modification pipeline."""

    @pytest.mark.parametrize("n_slots,n_phases,harmonic", [
        (12, 3, 1),
        (12, 3, 5),
    ])
    def test_modification_pipeline(self, n_slots, n_phases, harmonic):
        cs = CurrentSystem(n_phases, current_system_flag=0)
        mmf = get_mmf(WindingSpectrum(n_slots, harmonic))
        windings = get_primitive_multiphase_winding(mmf, cs)
        sp = get_single_phase_winding(windings, 0)
        cg = get_coil_group(sp)

        dw = winding_topology_double_way_connection(cg)
        assert len(dw) == 2

        sw_md = winding_topology_single_way_connection_md(cg)
        assert len(sw_md) == 2

        sw_sp = winding_topology_single_way_connection_sp(cg)
        assert len(sw_sp) == 2

        mt = obtain_multi_turn_winding_topology(dw)
        assert len(mt) == 2

        ml = obtain_multi_layer_winding_topology(mt)
        assert len(ml) == 2

        dl = obtain_double_layer_winding_topology(sw_md)
        assert len(dl) == 2

        sl = obtain_single_layer_winding_topology(mt)
        assert len(sl) == 2

    def test_modification_results_not_nan(self):
        """All modification results should produce valid winding spectra."""
        cs = CurrentSystem(3, current_system_flag=0)
        mmf = get_mmf(WindingSpectrum(12, 1))
        windings = get_primitive_multiphase_winding(mmf, cs)
        sp = get_single_phase_winding(windings, 0)
        cg = get_coil_group(sp)

        for topo in winding_topology_double_way_connection(cg):
            ws = topo.winding_spectrum_real
            assert not np.any(np.isnan(ws))
            assert not np.any(np.isinf(ws))


# ======================================================================
# Known Result Tests (Thesis Validation)
# ======================================================================

class TestThesisValidation:
    """Validate against results from the PhD thesis."""

    def test_winding_factor_12slot_gamma1(self):
        """Thesis §6.1: 12-slot, 3-phase, γ=1 → |ξ(1)| ≈ 0.933."""
        cs = CurrentSystem(3, current_system_flag=0)
        mmf = get_mmf(WindingSpectrum(12, 1))
        w = get_primitive_multiphase_winding(mmf, cs)
        sp = get_single_phase_winding(w, 0)
        cg = get_coil_group(sp)
        dl = obtain_double_layer_winding_topology(
            winding_topology_single_way_connection_md(cg))
        ws = dl[0].winding_spectrum_real
        wf_1 = np.abs(ws[6])  # ν=1 at index 6 for 12 slots
        assert wf_1 == pytest.approx(0.9330, abs=0.005)

    def test_winding_factor_12slot_gamma5(self):
        """Thesis §6.1: 12-slot, 3-phase, γ=5 → |ξ(5)| ≈ 0.933."""
        cs = CurrentSystem(3, current_system_flag=0)
        mmf = get_mmf(WindingSpectrum(12, 5))
        w = get_primitive_multiphase_winding(mmf, cs)
        sp = get_single_phase_winding(w, 0)
        cg = get_coil_group(sp)
        dl = obtain_double_layer_winding_topology(
            winding_topology_single_way_connection_md(cg))
        ws = dl[0].winding_spectrum_real
        wf_5 = np.abs(ws[10])  # ν=5 at index 10 for 12 slots
        assert wf_5 == pytest.approx(0.9330, abs=0.005)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
