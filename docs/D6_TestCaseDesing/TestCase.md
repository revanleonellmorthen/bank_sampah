> **Catatan:** dokumen ini versi lama dan sudah digantikan oleh
> [`docs/D6-Test-Case-Design.md`](../D6-Test-Case-Design.md), yang memakai tarif
> resmi D1 (Plastik 3 poin/kg, Nonplastik 2 poin/kg) dan 11 test case.
> Tarif 1.000 poin/kg di bawah ini tidak dipakai lagi.

# D6. Test Case Design (1 Scenario)

**Skenario yang Dipilih:** Skenario 1 - Input Setoran Sampah (Petugas)

Berikut adalah rancangan pengujian (*test case*) untuk memastikan alur input setoran sampah berjalan dengan benar dan aman dari *error*.

---

## Penghitungan Poin Setoran Sampah
Skenario ini menguji fungsi penghitungan konversi sampah menjadi poin pada modul **03 Pencatatan Setoran** dan **04 Poin & Dompet**. Sistem menghitung poin berdasarkan berat aktual yang ditimbang, jenis kategori sampah yang dipilih, dan status hari (apakah menerapkan pengali bonus akhir pekan atau tidak).

### Asumsi
*   Tarif poin contoh: Plastik = 1.000 poin/kg, Kertas = 500 poin/kg.
*   Batas maksimal berat per transaksi: 100 kg (mencegah *input* angka tidak wajar).
*   Berat desimal diizinkan hingga 2 angka di belakang koma (contoh: 1.25 kg).
*   Tarif yang digunakan adalah tarif yang berlaku saat transaksi disimpan (bukan saat form dibuka).
*   *Weekend Multiplier*: Jika fitur aktif, transaksi pada hari Sabtu/Minggu akan mendapatkan pengali 2x.
*   Satu transaksi setoran = satu ID referensi unik (anti-duplikasi).
*   Tarif dan batas maksimal merupakan nilai contoh yang dapat diubah oleh Admin melalui konfigurasi sistem.

### Aturan Perhitungan
1. Sistem mencatat ID Warga, Kategori Sampah, dan Berat (kg).
2. Sistem mengambil tarif dasar berdasarkan kategori dari Modul Master Data.
3. Sistem mengecek apakah hari ini Sabtu/Minggu dan apakah *toggle* bonus akhir pekan aktif.
4. Poin Normal dihitung dengan mengalikan Berat dengan Tarif Dasar.
5. Jika bonus akhir pekan aktif, Poin Akhir = Poin Normal × 2.
6. Jika berat kurang dari atau sama dengan 0, atau melebihi 100 kg, sistem menolak transaksi dan mengembalikan pesan *error*.

---

## Tabel Test Case

| ID | Title | Type | Preconditions | Input / Steps | Expected Result | Alasan Pemilihan (Rationale) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Input setoran sampah dengan data valid | Common | Petugas sudah login; Data warga terdaftar; Tarif Plastik aktif (1.000/kg); Hari kerja (bukan weekend). | 1. Cari ID Warga.<br>2. Pilih Kategori "Plastik".<br>3. Input berat `5` kg.<br>4. Klik "Simpan". | Transaksi sukses. Saldo warga bertambah **5.000 poin** (5 kg x 1.000). Status transaksi *Verified*. | Kami memilih ini sebagai *common case* untuk memvalidasi alur utama (*happy path*) sesuai diagram *sequence*. Pengujian ini memastikan fungsi inti berjalan sesuai harapan. |
| **TC-02** | Input setoran dengan *Double-Click* akibat koneksi lambat | Edge | Petugas sudah login; Jaringan internet sedang lambat (*lagging*). | 1. Input data setoran dengan berat `5` kg.<br>2. Petugas tidak sengaja mengklik tombol "Simpan" dua kali secara cepat karena mengira sistem *hang*. | Sistem **hanya memproses 1 transaksi**. Saldo warga hanya bertambah 5.000 poin sekali (mencegah *bug duplicate entry*). | Kami memilih skenario ini karena kejadian *double-click* sangat *random* namun sering terjadi di lapangan akibat sinyal buruk. Jika *backend* tidak dilengkapi pengaman *Idempotency*, sistem bisa menggandakan saldo secara tidak sah. |
| **TC-03** | Input setoran melebihi batas maksimal berat | Edge | Petugas sudah login. | 1. Cari ID Warga.<br>2. Pilih Kategori "Plastik".<br>3. Input berat `150` kg (melebihi batas 100 kg).<br>4. Klik "Simpan". | Sistem menolak transaksi. Muncul pesan *error* "Berat melebihi batas maksimal (100 kg)". | Kami memilih ini untuk memvalidasi *boundary value* (batas atas). Mencegah petugas salah ketik angka (misal: mengetik 1500 kg padahal maksudnya 15.0 kg) yang bisa merusak integritas data dan "membludakkan" poin warga. |
