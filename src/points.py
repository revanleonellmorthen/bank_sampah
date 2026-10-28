"""Kalkulasi poin setoran sampah (D7)."""

from math import floor

# Tarif dasar poin per kg (lihat D1). Weekend multiplier x2.
RATE_TABLE = {
    "Plastik": 3,
    "Nonplastik": 2,
}
WEEKEND_MULTIPLIER = 2
MAX_WEIGHT_KG = 100  # batas wajar satu transaksi setoran


def calculate_points(waste_type, weight_kg, on_weekend=False):
    """Hitung poin dari jenis sampah dan berat (kg), dibulatkan half-up ke integer."""
    if waste_type not in RATE_TABLE:
        raise ValueError(f"Kategori sampah tidak dikenal: {waste_type!r}")
    if isinstance(weight_kg, bool) or not isinstance(weight_kg, (int, float)):
        raise ValueError(f"Berat harus berupa angka, bukan {type(weight_kg).__name__}")
    if weight_kg <= 0:
        raise ValueError("Berat harus lebih dari 0 kg")
    if weight_kg > MAX_WEIGHT_KG:
        raise ValueError(f"Berat melebihi batas {MAX_WEIGHT_KG} kg")

    rate = RATE_TABLE[waste_type] * (WEEKEND_MULTIPLIER if on_weekend else 1)
    return floor(weight_kg * rate + 0.5)
