# D2. Pemecahan Modul (*Module Breakdown*)

Untuk memastikan aplikasi mudah dipelihara (*maintainable*), mudah diuji (*testable*), dan dapat dikembangkan lebih lanjut di masa depan (*scalable*), arsitektur sistem EcoSmart Waste Bank dipecah menjadi **5 modul inti** yang saling terisolasi secara fungsional (*Separation of Concerns*).

---

## 1. Modul Autentikasi & Manajemen Akun (`Auth & Account Module`)
* **Tanggung Jawab:** 
  Modul ini bertindak sebagai penjaga keamanan terdepan (*security gateway*). Tanggung jawab utamanya adalah mengelola siklus hidup identitas pengguna, melindungi akses rute aplikasi melalui verifikasi token (*JWT*), serta memastikan batasan otorisasi antara Warga, Petugas, dan Admin berjalan dengan ketat.
* **Fitur Utama:**
  * **Registrasi & Validasi:** Pendaftaran mandiri warga baru (menggunakan NIK/KTP atau Email mahasiswa) dan pendaftaran petugas yang hanya bisa diinisiasi oleh Admin.
  * **Otentikasi Aman:** Mekanisme Login/Logout dengan pembuatan sesi berbatas waktu (*time-bound Session Token*).
  * **Kontrol Akses Berbasis Peran (*Role-Based Access Control / RBAC*):** Memblokir warga agar tidak bisa mengakses halaman input setoran milik petugas, dan sebaliknya.
  * **Manajemen Profil:** Pembaruan data demografi pengguna (nomor telepon aktif, alamat, dan penggantian *password*).

## 2. Modul Pencatatan Setoran (`Deposit Recording Module`)
* **Tanggung Jawab:** 
  Modul ini adalah jantung operasional harian yang melayani interaksi langsung antara petugas dan nasabah. Tanggung jawabnya adalah memastikan bahwa setiap keping sampah yang ditimbang terekam dengan akurat ke dalam basis data lengkap dengan *timestamp* (waktu transaksi), identitas nasabah, dan takaran beratnya.
* **Fitur Utama:**
  * **Antarmuka Kasir Setoran (*Point of Deposit UI*):** Halaman cepat bagi petugas untuk mencari ID Warga, memilih *dropdown* jenis sampah (Plastik / Nonplastik), dan memasukkan input angka berat sampah (kg).
  * **Penyaringan & Validasi Masukan:** Memastikan angka berat yang di-input tidak bernilai minus, dan memperingatkan petugas jika *input* berat dinilai tidak wajar (misalnya salah ketik 1000 kg).
  * **Penandaan Status Transaksi:** Mengklasifikasikan status log setoran (contoh: *Verified* jika petugas sudah menyetujui, *Cancelled* jika terjadi kesalahan catat).
  * **Buku Riwayat Setoran (*Deposit History Log*):** Menampilkan daftar riwayat kapan saja warga telah membuang sampah, yang dapat difilter berdasarkan bulan dan tahun.

## 3. Modul Poin & Dompet Digital (`Points & Wallet Module`)
* **Tanggung Jawab:** 
  Berfungsi sebagai mesin kecerdasan logika bisnis (*business logic engine*) utama di dalam aplikasi. Modul ini bertanggung jawab mengalkulasi konversi poin secara otonom berdasarkan waktu transaksi, serta menjaga integritas buku besar (*ledger*) agar saldo nasabah akurat dan tidak pernah defisit (minus).
* **Fitur Utama:**
  * **Kalkulator Poin Dinamis (*Rules Engine*):** Memeriksa hari dari *timestamp* setoran. Jika Senin-Jumat, menerapkan *Base Rate* (Plastik: 3, Nonplastik: 2). Jika terdeteksi Sabtu/Minggu, secara otomatis memicu fungsi *Weekend Multiplier* (Plastik: 6, Nonplastik: 4).
  * **Mutasi Akuntansi (*Ledger System*):** Mencatat setiap perubahan poin sebagai *Credit* (penambahan dari setoran) atau *Debit* (pengurangan dari penukaran) dengan prinsip ketertelusuran tinggi (*audit trail*).
  * **Penjaga Integritas Saldo:** Fungsi validasi ketat yang akan secara otomatis menolak dan membatalkan transaksi penukaran (*rollback*) jika terdeteksi poin nasabah tidak mencukupi (Mencegah bug saldo negatif).

## 4. Modul Penukaran Hadiah (`Reward Redemption Module`)
* **Tanggung Jawab:** 
  Modul ini menangani pengalaman *rewarding* bagi nasabah. Tanggung jawabnya mencakup pengelolaan katalog produk/hadiah dari mitra kerja sama, pengecekan ketersediaan stok hadiah fisik/digital, serta penerbitan token klaim kepada pengguna.
* **Fitur Utama:**
  * **Manajemen Etalase Katalog:** Menampilkan daftar (*list*) hadiah yang tersedia (contoh: "Voucher Sembako Rp50.000", "Pulsa Rp20.000") lengkap dengan harga tukar poinnya dan sisa stok kuota harian.
  * **Proses *Checkout* Penukaran:** Menangkap permintaan penukaran warga, mengunci stok hadiah, dan berkoordinasi dengan *Points & Wallet Module* untuk melakukan pemotongan saldo secara atomik.
  * **Pembangkit Kode Voucher (*Voucher Generator*):** Menciptakan kode unik (misal: `ECO-RW-2026-X8B9`) yang akan muncul di layar warga, yang nantinya ditunjukkan kepada petugas untuk menerima barang/hak hadiah fisiknya.

## 5. Modul Pelaporan & Notifikasi (`Reporting & Notification Module`)
* **Tanggung Jawab:** 
  Bertindak sebagai pusat pemantauan performa dan komunikasi eksternal. Modul ini bertanggung jawab merangkum data mentah menjadi informasi visual bagi pihak manajemen (Admin), serta memastikan warga mendapat kepastian informasi atas transaksi mereka secara *real-time*.
* **Fitur Utama:**
  * **Dasbor Statistik Keseluruhan:** Menampilkan grafik interaktif yang menyajikan data tren volume sampah bulanan, sebaran rasio sampah Plastik vs Nonplastik, serta jumlah poin yang telah dicetak dan diklaim dalam sistem.
  * **Ekspor Data (*Data Export*):** Memungkinkan Admin untuk mengunduh laporan ke dalam bentuk *CSV/Excel* untuk diserahkan sebagai laporan pertanggungjawaban kepada institusi, desa, atau sponsor.
  * **Sistem Pemberitahuan (*In-App Alerts*):** Memicu pengiriman pesan ke aplikasi (*dashboard alert*) warga secara otomatis sesaat setelah petugas selesai memasukkan data timbangan, memberitahu warga: *"Setoran berhasil! Anda mendapatkan 12 poin."*

---

## Matriks Ketergantungan Modul (*Module Dependencies Matrix*)

Agar aplikasi terintegrasi dengan mulus namun tetap longgar (*loosely coupled*), antar modul berkomunikasi mengikuti alur berikut:

| Modul Penginisiasi (*Caller*) | Modul Tujuan (*Target*) | Deskripsi Alur Data & Ketergantungan Teknis |
| :--- | :--- | :--- |
| **Auth Module** | *Semua Modul Terlindungi* | Setiap modul (Pencatatan, Penukaran, Pelaporan) bergantung pada Auth untuk memastikan *Token Session JWT* valid sebelum data ditampilkan kepada pengguna di rute yang sedang diakses. |
| **Deposit Recording** | **Points & Wallet** | Ini adalah **jalur komunikasi paling krusial**. Begitu petugas menekan tombol 'Simpan Setoran', modul Pencatatan langsung "memanggil" modul Dompet untuk mengirim parameter `(ID_Warga, Jenis_Sampah, Berat_Kg, Waktu)`. Dompet kemudian menghitung poin dan memperbarui saldo warga tersebut. |
| **Reward Redemption** | **Points & Wallet** | Saat warga menekan 'Tukar Hadiah', modul Penukaran bertanya kepada modul Dompet: *"Apakah Saldo Warga-A >= Harga Hadiah?"* Jika *True*, Dompet memotong poin, lalu Penukaran menerbitkan kode voucher. Jika *False*, transaksi ditolak di tempat. |
| **Reporting & Notification** | *Deposit* & *Redemption* | Modul Pelaporan bersifat *Read-Only* (Hanya membaca). Modul ini secara berkala mengambil agregat data (metode `SELECT/COUNT/SUM`) dari tabel log milik Modul Pencatatan dan Penukaran untuk dirender ke dalam bentuk laporan visual. |
