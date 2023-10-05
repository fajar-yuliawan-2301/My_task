from datetime import datetime

tanggal_lahir = int(input('Masukan Tanggal Lahir: '))
bulan_lahir = int(input('Masukan Bulan lahir: '))
tahun_lahir = int(input('Masukan Tahun Lahir: '))

tanggal_sekarang = datetime.now().day
bulan_sekarang = datetime.now().month
tahun_sekarang = datetime.now().year

selisih_tahun = tahun_sekarang - tahun_lahir
selisih_bulan = bulan_sekarang - bulan_lahir
selisih_hari = tanggal_sekarang - tanggal_lahir

if selisih_hari < 0:
    selisih_bulan -= 1
    selisih_hari += 30

if selisih_bulan < 0:
    selisih_tahun -= 1
    selisih_tahun += 12

print(f"Umur anda: {selisih_tahun} tahun {selisih_bulan} bulan {selisih_hari} hari")
