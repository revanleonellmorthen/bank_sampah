# Bank Sampah Digital

## Deskripsi Singkat
Aplikasi bank sampah digital untuk merecord setoran bank sampah bagi warga dan membuat laporan pengumuplan sampah bagi petugas

---

## Anggota Tim

| Nama | NIM | Username GitHub |
| :--- | :--- | :--- |
| Sutan Lutfi Frank Richard | 26110300033 | [@lutfifr31](https://github.com/lutfifr31) |
| Revan Leonell Morthen | 26110300004 | [@revanleonellmorthen](https://github.com/revanleonellmorthen) |
| Muhammad Hizqil Zakaria | 26110300009 | [@ReHizqil23](https://github.com/ReHizqil23) |

---

## Daftar Deliverable

| Kode | Deliverable | Link |
| :--- | :--- | :--- |
| D1 | Topic & Problem Statement | [Link](docs/D1-Problem_&_statement.md) |
| D2 | [Nama Deliverable 2] | [Link](https://link-anda-di-sini) |
| D3 | Usecase | [Link](docs/D3_Usecase_Diagram) |
| D4 | Sequence & Scenario | [Link](docs/D4-Sequence-diagram) |
| D6 | Test Case Design | [Link](docs/D6-Test-Case-Design.md) |
| D7 | Unit-Tested Code | [Link](src/points.py) · [Test](tests/test_points.py) |

---

## Struktur Repo
Berikut adalah struktur direktori utama dalam repositori ini:

```text
├── docs/                  # Kumpulan dokumen (D1, D2, D3, dll)
├── src/                   # Kode sumber utama aplikasi
├── tests/                 # File pengujian (unit test / integration test)
├── README.md              # Dokumentasi utama proyek ini
```

---

## Cara Menjalankan Test

```bash
pip install pytest
python -m pytest
```

Semua test harus lulus (`11 passed`).

---


# Penggunaan AI dalam Pengembangan Proyek

Selama proses pengembangan proyek Sistem Bank Sampah Digital ini, kami memanfaatkan alat kecerdasan artifisial (AI). Penggunaan AI di sini murni berfungsi sebagai **partner diskusi (brainstorming partner)** dan asisten penulisan kode. Seluruh hasil *output* dari AI selalu kami tinjau, sesuaikan, dan perbaiki (*fix*) secara manual agar benar-benar sesuai dengan standar tugas.

Berikut adalah rincian implementasi penggunaan AI berdasarkan kontribusi masing-masing anggota:

| Alat AI | Pengguna | Digunakan Untuk | Contoh Penerapan / Implementasi |
| :--- | :--- | :--- | :--- |
| **DeepSeek AI** | Muhammad Hizqil Zakaria | *Brainstorming* Alur Sistem (D3) | Membantu merumuskan daftar fitur (use case) apa saja yang bisa dilakukan oleh aktor Warga, Petugas, dan Admin. **Finalisasi oleh kami:** Menyortir *use case* agar memenuhi syarat minimal 8, dan mengatur tata letak diagram agar lurus memanjang ke bawah (tanpa *package*) dengan relasi `<<include>>` dan `<<extend>>` yang tepat. |
| **DeepSeek AI** | Muhammad Hizqil Zakaria | Penyusunan Skenario (D4) | Membantu menyusun alur untuk 1 skenario utama (Skenario 1: Input Setoran Sampah) beserta alasan pemilihannya. **Finalisasi oleh kami:** Menyesuaikan detail alur *lifeline* (Aktor, UI, Modul) dan memvalidasi *alternative flow* (`alt`) agar logikanya sinkron dengan aturan bisnis. |
| **DeepSeek AI** | Muhammad Hizqil Zakaria | *Troubleshooting* & Dokumentasi | Membantu mencari solusi saat *library* PlantUML di GitHub Actions gagal berjalan karena masalah *Docker*. **Finalisasi oleh kami:** Memutuskan untuk mengabaikan *pipeline* otomatis tersebut dan mengekspor gambar secara manual ke format PNG demi efisiensi waktu, lalu merapikan *pathing* gambar di file `README.md`. |
| ... | ... | ... | ... |
