# D3. Use Case Diagram - Bank Sampah Digital

Dokumen ini memuat visualisasi *Use Case Diagram* untuk Sistem Bank Sampah Digital beserta penjelasan singkat dari masing-masing modul.

---

## Diagram Utuh (Whole System)
Diagram ini menggambarkan keseluruhan interaksi antara aktor (Warga, Petugas, Admin) dengan sistem bank sampah digital. Seluruh *use case* dikelompokkan berdasarkan 6 modul utama untuk memudahkan pemahaman alur kerja sistem secara menyeluruh.

![Whole System](./img/mainmodul.png)

---

## Diagram Per Modul

### 1. Modul Autentikasi & Otorisasi
Modul ini berfokus pada keamanan akses sistem, mencakup proses login, registrasi, dan pengelolaan profil pengguna. Terdapat fitur pemulihan kata sandi (*Reset Password*) yang bersifat opsional (*extend*) jika pengguna mengalami kendala saat login.

![Autentikasi & Otorisasi](./img/modul1.png)

### 2. Modul Data Master
Modul ini dikhususkan untuk Admin dalam mengelola data referensi inti seperti tarif sampah, katalog hadiah, dan ketersediaan stok. Pengaturan parameter dinamis seperti bonus akhir pekan (*weekend multiplier*) juga diatur di sini agar sistem dapat beradaptasi dengan aturan bisnis yang berubah.

![Data Master](./img/modul2.png)

### 3. Modul Pencatatan Setoran
Modul ini memfasilitasi Petugas dalam mencatat setoran sampah fisik dari Warga secara akurat. Proses input setoran ini mewajibkan (*include*) kalkulasi poin otomatis agar saldo warga langsung diperbarui secara *real-time*.

![Pencatatan Setoran](./img/modul3.png)

### 4. Modul Poin & Dompet Digital
Modul ini memberikan transparansi kepada Warga untuk memantau saldo poin aktif dan melihat riwayat mutasi (buku tabungan digital). Modul ini berfungsi sebagai buku besar (*ledger*) yang memastikan integritas finansial digital pengguna tetap terjaga.

![Poin & Dompet Digital](./img/modul4.png)

### 5. Modul Penukaran Hadiah
Modul ini menangani alur penukaran poin menjadi hadiah oleh Warga melalui etalase katalog yang tersedia. Proses penukaran secara otomatis mewajibkan (*include*) pengecekan stok, pemotongan saldo, dan penerbitan voucher unik sebagai bukti klaim yang sah.

![Penukaran Hadiah](./img/modul5.png)

### 6. Modul Pelaporan & Notifikasi
Modul ini berfungsi sebagai pusat intelijen bisnis yang menyajikan dasbor analitik dan fitur ekspor laporan bagi Admin. Selain itu, modul ini menjembatani komunikasi ke Warga melalui pengiriman notifikasi terkait status setoran maupun penukaran hadiah.

![Pelaporan & Notifikasi](./img/modul6.png)
