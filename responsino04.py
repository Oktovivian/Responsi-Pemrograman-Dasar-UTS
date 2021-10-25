status_pegawai = input("Masukkan status pegawai (Tetap/Kontak): ")

gaji = 4000000
if status_pegawai == 'Tetap':
    jumlah_anak = int(input("Masukkan jumlah anak: "))
    if jumlah_anak <= 3:
        tunjangan = 220000 * jumlah_anak
        gaji = gaji + tunjangan
    elif jumlah_anak > 3:
        tunjangan =  200000 * jumlah_anak
        gaji = gaji + tunjangan
elif status_pegawai == 'Kontrak':
    gaji = 4000000

print("Gaji anda adalah",gaji)

