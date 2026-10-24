# D3. Use Case Diagram - Bank Sampah Digital

Dokumen ini memuat visualisasi *Use Case Diagram* untuk Sistem Bank Sampah Digital. Diagram dibuat menggunakan **PlantUML** dan dikelompokkan berdasarkan modul.

> **Catatan:** Jika gambar di bawah ini belum muncul (hanya menampilkan ikon patah), berarti *GitHub Actions* sedang dalam proses mengubah file `.puml` menjadi `.svg`. Silakan *refresh* halaman setelah beberapa saat.

---

## Diagram Utuh (Whole System)
Diagram ini mencakup seluruh sistem, memetakan semua aktor (Warga, Petugas, Admin), dan mengelompokkan *use case* berdasarkan modulnya.

![Whole System](./WholeSystem.svg)

---

## Diagram Per Modul

### 1. Modul Autentikasi & Otorisasi
![Autentikasi & Otorisasi](./01-auth.svg)

### 2. Modul Data Master
![Data Master](./02-masterdata.svg)

### 3. Modul Pencatatan Setoran
![Pencatatan Setoran](./03-deposit.svg)

### 4. Modul Poin & Dompet Digital
![Poin & Dompet Digital](./04-points-wallet.svg)

### 5. Modul Penukaran Hadiah
![Penukaran Hadiah](./05-redemptions.svg)

### 6. Modul Pelaporan & Notifikasi
![Pelaporan & Notifikasi](./06-reporting.svg)
