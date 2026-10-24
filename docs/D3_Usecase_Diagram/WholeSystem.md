@startuml
left to right direction
skinparam packageStyle rectangle
skinparam usecase {
  BackgroundColor LightBlue
  BorderColor DarkBlue
}

' --- AKTOR ---
actor "Warga" as Warga
actor "Petugas" as Petugas
actor "Admin" as Admin

' --- SISTEM UTAMA ---
rectangle "Sistem Bank Sampah Digital" {
  
  ' --- MODUL 1 ---
  package "1. Autentikasi & Otorisasi" {
    usecase "Login" as UC_Login
    usecase "Registrasi Akun" as UC_Registrasi
    usecase "Kelola Profil" as UC_Profil
    usecase "Reset Password" as UC_Reset
  }

  ' --- MODUL 2 ---
  package "2. Data Master" {
    usecase "Kelola Tarif & Kategori Sampah" as UC_Tarif
    usecase "Kelola Katalog & Stok Hadiah" as UC_Hadiah
  }

  ' --- MODUL 3 & 4 ---
  package "3 & 4. Pencatatan & Poin" {
    usecase "Input Setoran Sampah" as UC_Setoran
    usecase "Kalkulasi Poin Otomatis" as UC_Kalkulasi
    usecase "Lihat Buku Tabungan" as UC_Passbook
  }

  ' --- MODUL 5 ---
  package "5. Penukaran Hadiah" {
    usecase "Tukar Poin (Redeem)" as UC_Redeem
    usecase "Cek Stok Real-Time" as UC_CekStok
    usecase "Terbitkan Voucher Unik" as UC_Voucher
  }

  ' --- MODUL 6 ---
  package "6. Pelaporan & Notifikasi" {
    usecase "Lihat Dasbor Analitik" as UC_Dasbor
    usecase "Ekspor Laporan (CSV/Excel)" as UC_Ekspor
    usecase "Lihat Notifikasi In-App" as UC_Notif
  }
}

' --- RELASI AKTOR KE USE CASE ---
Warga --> UC_Registrasi
Warga --> UC_Login
Warga --> UC_Profil
Warga --> UC_Passbook
Warga --> UC_Redeem
Warga --> UC_Notif

Petugas --> UC_Login
Petugas --> UC_Setoran

Admin --> UC_Login
Admin --> UC_Tarif
Admin --> UC_Hadiah
Admin --> UC_Dasbor
Admin --> UC_Ekspor

' --- RELASI INCLUDE & EXTEND ---
UC_Reset .> UC_Login : <<extend>>
UC_Setoran .> UC_Kalkulasi : <<include>>
UC_Redeem .> UC_CekStok : <<include>>
UC_Redeem .> UC_Voucher : <<include>>

@enduml
