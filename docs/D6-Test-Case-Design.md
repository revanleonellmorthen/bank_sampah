# D6. Test Case Design — Skenario 1: Input Setoran Sampah

Dokumen ini memuat rancangan *test case* untuk skenario **Input Setoran Sampah** (lihat [D4](../docs/D4-Sequence-diagram/skenario1.md)), yaitu alur petugas mencatat setoran warga dan sistem mengonversi berat sampah menjadi poin. Fungsi yang diuji di D7 adalah `calculate_points(waste_type, weight_kg, on_weekend)`.

## Tabel Test Case

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Setoran plastik pada hari kerja | Common | Petugas login; tarif Plastik = 3 poin/kg | Input kategori `Plastik`, berat `2.45` kg, hari kerja | Transaksi tersimpan, warga menerima **7 poin** |
| TC-02 | Setoran nonplastik pada hari kerja | Common | Petugas login; tarif Nonplastik = 2 poin/kg | Input kategori `Nonplastik`, berat `3.0` kg, hari kerja | Warga menerima **6 poin** |
| TC-03 | Setoran plastik pada akhir pekan | Common | Petugas login; weekend multiplier aktif | Input kategori `Plastik`, berat `1.0` kg, hari Sabtu | Warga menerima **6 poin** (tarif 3 x 2) |
| TC-04 | Setoran nonplastik pada akhir pekan | Common | Petugas login; weekend multiplier aktif | Input kategori `Nonplastik`, berat `2.5` kg, hari Minggu | Warga menerima **10 poin** (tarif 2 x 2 x 2,5 kg) |
| TC-05 | Setoran berat kecil dengan pembulatan | Common | Petugas login | Input kategori `Plastik`, berat `0.5` kg, hari kerja | Hasil 1,5 poin dibulatkan ke atas menjadi **2 poin** |
| TC-06 | Berat nol | Edge | Petugas login | Input berat `0` kg | Sistem menolak dengan pesan "Berat harus lebih dari 0 kg"; saldo warga tidak berubah |
| TC-07 | Berat negatif | Edge | Petugas login | Input berat `-1.2` kg | Sistem menolak input; tidak ada transaksi tersimpan |
| TC-08 | Berat melebihi batas wajar | Edge | Petugas login | Input berat `150` kg (batas 100 kg) | Sistem menolak dengan pesan "Berat melebihi batas 100 kg" |
| TC-09 | Kategori sampah tidak dikenal | Edge | Petugas login | Input kategori `Kaca` (tidak ada di tabel tarif) | Sistem menolak dengan pesan "Kategori sampah tidak dikenal" |
| TC-10 | Pembulatan tepat setengah | Edge | Petugas login | Input kategori `Nonplastik`, berat `1.25` kg, hari kerja (hasil 2,5 poin) | Dibulatkan *half-up* menjadi **3 poin**, bukan 2 |
| TC-11 | Berat bukan angka | Edge | Petugas login | Input berat `"dua"` (teks) | Sistem menolak dengan pesan "Berat harus berupa angka" |

Total: **11 test case** — 5 *common*, 6 *edge*. Semua TC di atas diimplementasikan sebagai unit test di [`tests/test_points.py`](../tests/test_points.py) dengan ID yang sama (TC-01 s.d. TC-11).

## Cara Memilih Edge Case

Edge case dipilih dari titik tempat perhitungan poin bisa merugikan salah satu pihak. Pertama, batas bawah berat (nol dan negatif) karena input manual dari timbangan rawan salah ketik dan berat negatif akan mengurangi saldo warga. Kedua, batas atas berat untuk menangkap salah ketik seperti `25` menjadi `250` kg yang bisa membengkakkan poin. Ketiga, kategori di luar tabel tarif, karena data master bisa berubah dan sistem tidak boleh menebak tarif. Keempat, pembulatan tepat setengah (2,5 poin) karena aturan pembulatan harus konsisten dan tidak bergantung pada *banker's rounding* bawaan Python. Terakhir, input bukan angka, karena nilai dari form HTML bisa sampai ke logika perhitungan sebagai teks.
