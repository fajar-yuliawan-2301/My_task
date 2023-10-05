# 1. Mulai
# 2. Masukan nilai panjang
# 3. Masukan nilai lebar
# 4. Masukan nilai tinggi
# 5. Hitung luas balok yang disimpan pada variabel luas dengan proses berikut:
# 6. luas = (2 x p x l) + (2 x p x t) + (2 x l x t)
# 7. Hitung volume balok yang disimpan pada variabel volume dengan proses berikut:
# 8. volume = p x l x t
# 9. keliling = 2 * (panjang + lebar + tinggi)
# 10. Tampilkan nilai luas.
# 11. Tampilkan nilai volume.
# 12. Tampilan nilai keliling
# 13. Selesai.

panjang = float(input('Masukan Panjang:'))
lebar = float(input('Masukan Lebar:'))
tinggi = float(input('Masukan Tinggi:'))

luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
volume = panjang * lebar * tinggi
keliling = 2 * (panjang + lebar + tinggi)

print('Luas :',round(luas))
print('Volume :',round(volume))
print('Keliling :',round(keliling))
