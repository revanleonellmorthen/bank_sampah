# D1. Topik & Pernyataan Masalah (*Topic & Problem Statement*)

## 1. Nama Aplikasi & Deskripsi Singkat
* **Nama Aplikasi:** **EcoSmart Waste Bank** (*Digital Waste Management & Point Reward Platform*)
* **Deskripsi Singkat:** 
  EcoSmart Waste Bank adalah platform perangkat lunak berbasis *web* dan *mobile* yang dirancang untuk merevolusi tata kelola bank sampah komunitas konvensional menjadi ekosistem ekonomi sirkular yang sepenuhnya digital. Aplikasi ini memfasilitasi pencatatan setoran sampah secara akurat, di mana warga dapat menyerahkan sampah yang telah dipilah (plastik dan nonplastik) kepada petugas untuk diverifikasi dan dicatat ke dalam sistem. Sebagai bentuk apresiasi dan gamifikasi untuk membangun kebiasaan daur ulang, sistem secara otomatis mengonversi berat sampah menjadi poin digital berdasarkan matriks tarif yang dinamis—termasuk fitur *weekend multiplier* (poin ganda di akhir pekan). Poin yang terkumpul berfungsi sebagai mata uang virtual di dalam aplikasi yang dapat ditukarkan (*redeem*) secara instan dengan berbagai hadiah menarik seperti voucher belanja ritel, pengisian pulsa seluler, hingga diskon produk dari mitra lokal. Platform ini memastikan transparansi total bagi nasabah, sekaligus menyederhanakan pelaporan administratif bagi pengelola bank sampah.

---

## 2. Masalah (*The Problem*)
* **Siapa yang memiliki masalah ini?** 
  1. **Warga Perkotaan / Komunitas Kampus (Nasabah):** Individu, mahasiswa, atau rumah tangga yang memiliki niat baik untuk mendaur ulang sampah mereka, namun membutuhkan sistem pencatatan tabungan yang transparan dan fleksibel.
  2. **Petugas Operasional Bank Sampah:** Relawan atau staf lapangan yang bertugas menerima, menimbang, dan mencatat setoran sampah warga di lokasi pengumpulan.
  3. **Pengelola / Ketua Bank Sampah:** Pihak manajemen yang membutuhkan data analitik mengenai total volume sampah yang berhasil dikurangi dan sirkulasi keuangan (poin/hadiah) untuk pelaporan ke instansi pemerintah atau mitra sponsor.

* **Bagaimana mereka menanganinya saat ini?** 
  Saat ini, operasional bank sampah di tingkat RT/RW maupun kampus sangat bergantung pada sistem pencatatan manual (*paper-based system*). Warga harus datang dengan membawa buku tabungan fisik berwujud kertas. Ketika sampah ditimbang, petugas harus membuka buku besar (*logbook* tebal), mencari nama warga secara manual, menghitung konversi berat ke nominal saldo menggunakan kalkulator, lalu menuliskan hasilnya dengan pena di buku besar dan buku tabungan warga. Laporan bulanan dibuat dengan merekap ratusan baris data dari buku besar ke dalam Microsoft Excel secara manual oleh pengelola.

* **Mengapa hal tersebut sangat menyulitkan (*painful*)?**
  1. **Tingkat Transparansi dan Kepercayaan yang Rendah:** Buku tabungan fisik sangat rentan rusak, basah, atau hilang. Jika hilang, warga seringkali kehilangan seluruh riwayat saldo poin mereka karena pencocokan data dengan buku besar milik petugas sangat memakan waktu. Hal ini membuat warga malas untuk terus berpartisipasi.
  2. **Risiko *Human Error* yang Fatal:** Menghitung konversi berat sampah (misalnya 1,35 kg) menjadi poin di tengah antrean warga yang panjang sangat berisiko memicu salah hitung atau salah tulis (*typo*), yang pada akhirnya merugikan nasabah atau merugikan kas bank sampah.
  3. **Beban Administratif Pelaporan:** Pengelola menghabiskan waktu berhari-hari setiap akhir bulan hanya untuk melakukan rekapitulasi data. Mereka kesulitan melacak secara *real-time* berapa kapasitas sampah yang terkumpul hari ini, atau berapa beban utang poin yang belum ditukarkan oleh warga.
  4. **Sistem Insentif yang Kaku dan Tidak Menarik:** Karena dihitung manual, bank sampah konvensional tidak bisa menerapkan strategi *marketing* yang dinamis (seperti "Hari Bumi: Poin x3" atau "Poin Ganda di Akhir Pekan") karena akan sangat membingungkan petugas lapangan yang mencatat.

---

## 3. Target Pengguna / Aktor (*Target Users / Actors*)
Sistem ini membagi batas wewenang berdasarkan tiga profil aktor utama, yaitu:
1. **Warga / Nasabah (*Resident*):** 
   * Aktor utama yang menjadi roda penggerak penyetoran sampah.
   * *Kebutuhan Utama:* Ingin melihat saldo poin secara *real-time*, melihat riwayat setoran secara detail (tanggal, berat, kategori), dan menelusuri katalog hadiah untuk menukarkan poin secara mandiri lewat *smartphone*.
2. **Petugas Bank Sampah (*Waste Bank Officer*):** 
   * Aktor operasional yang memegang kendali atas validitas data fisik.
   * *Kebutuhan Utama:* Membutuhkan antarmuka input data yang cepat (*fast-entry UI*) untuk memasukkan ID Warga, jenis sampah, dan berat timbangan secara instan, serta memverifikasi penukaran kode voucher saat warga mengklaim hadiah secara fisik.
3. **Admin Sistem (*System Administrator*):** 
   * Aktor super-user yang mengelola keberlangsungan bisnis platform.
   * *Kebutuhan Utama:* Memiliki wewenang untuk menambah/menghapus akun petugas, mengubah rasio poin per kilogram sampah, mengelola ketersediaan stok hadiah di katalog, serta mengekspor laporan bulanan (*PDF/CSV*).

---

## 4. Ruang Lingkup Sistem (*Project Scope*)

### Apa yang AKAN dilakukan oleh aplikasi (*In-Scope*):
1. **Pencatatan Setoran Transaksional Digital:** Menyediakan modul input bagi petugas untuk mendaftarkan transaksi penyetoran warga berdasarkan kategori pemilahan baku (Plastik dan Nonplastik) dengan nilai berat spesifik hingga dua desimal (misal: 2,45 kg), yang langsung terhubung ke basis data terpusat.
2. **Mesin Perhitungan Poin Dinamis (*Dynamic Point Engine*):** Memiliki algoritma otomatis yang menghitung perolehan hadiah berdasarkan parameter kalender, dengan aturan bisnis tetap: 
   * *Senin–Jumat:* 3 poin/kg untuk Plastik, 2 poin/kg untuk Nonplastik.
   * *Sabtu–Minggu (Weekend Multiplier):* 6 poin/kg untuk Plastik, 4 poin/kg untuk Nonplastik.
3. **Sistem Buku Besar Poin & Katalog Penukaran (*Ledger & Redemption*):** Mengelola mutasi saldo layaknya sistem perbankan digital. Sistem mengunci poin saat warga memilih hadiah dari direktori katalog (voucher belanja/pulsa/diskon) dan menerbitkan kode kupon digital unik *(Unique Redemption Code)* sebagai bukti klaim yang sah.
4. **Analitik & Pelaporan (*Dashboard & Reporting*):** Menampilkan dasbor ringkasan berupa grafik dan angka metrik utama (Total Kg Plastik Bulan Ini, Total Poin Beredar, Aktivitas Setoran Tertinggi) untuk keperluan evaluasi operasional oleh Admin.

### 3 hal yang TIDAK AKAN dilakukan aplikasi (*Out-of-Scope*):
1. **Tidak mencakup integrasi perangkat keras sensor IoT / Timbangan Pintar:** Seluruh input berat barang dilakukan secara manual *(manual entry)* oleh petugas melalui aplikasi (diketik dari hasil bacaan timbangan mekanik/digital biasa). Aplikasi berfokus murni pada solusi perangkat lunak manajemen data.
2. **Tidak menyediakan layanan logistik penjemputan sampah ke rumah (*Door-to-door Pick Up*):** Aplikasi ini tidak memiliki fitur pelacakan kurir atau pemesanan penjemputan. Model bisnis berfokus pada sistem *Drop-Off* di mana warga wajib datang secara mandiri ke titik lokasi bank sampah terdekat.
3. **Tidak melayani pencairan poin menjadi uang tunai digital (*E-Wallet/Bank Transfer*):** Untuk menghindari kerumitan regulasi keuangan negara (lisensi e-money dari Bank Indonesia), sistem sengaja dirancang agar poin (*closed-loop virtual currency*) hanya dapat ditukar dalam bentuk barang bernilai, diskon mitra, pulsa, atau voucher belanja internal, bukan transfer mata uang riil.
