"""Unit test untuk calculate_points (D7). ID test memetakan ke tabel D6."""

import pytest

from src.points import calculate_points


# --- Common cases (TC-01 .. TC-05) ---

def test_tc01_plastik_hari_biasa():
    assert calculate_points("Plastik", 2.45) == 7


def test_tc02_nonplastik_hari_biasa():
    assert calculate_points("Nonplastik", 3.0) == 6


def test_tc03_plastik_weekend():
    assert calculate_points("Plastik", 1.0, on_weekend=True) == 6


def test_tc04_nonplastik_weekend():
    assert calculate_points("Nonplastik", 2.5, on_weekend=True) == 10


def test_tc05_plastik_setengah_kilo_dibulatkan_ke_atas():
    assert calculate_points("Plastik", 0.5) == 2


# --- Edge cases (TC-06 .. TC-11) ---

def test_tc06_berat_nol_ditolak():
    with pytest.raises(ValueError):
        calculate_points("Plastik", 0)


def test_tc07_berat_negatif_ditolak():
    with pytest.raises(ValueError):
        calculate_points("Plastik", -1.2)


def test_tc08_berat_melebihi_batas_ditolak():
    with pytest.raises(ValueError):
        calculate_points("Plastik", 150)


def test_tc09_kategori_tidak_dikenal_ditolak():
    with pytest.raises(ValueError):
        calculate_points("Kaca", 1.0)


def test_tc10_pembulatan_tepat_setengah_half_up():
    # 1.25 kg x 2 poin = 2.5 -> 3 (bukan 2 seperti banker's rounding)
    assert calculate_points("Nonplastik", 1.25) == 3


def test_tc11_berat_bukan_angka_ditolak():
    with pytest.raises(ValueError):
        calculate_points("Plastik", "dua")
