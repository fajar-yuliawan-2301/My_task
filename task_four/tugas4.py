panjang = float(input('Masukan Panjang (cm):'))
lebar = float(input('Masukan Lebar (cm):'))
tinggi = float(input('Masukan Tinggi (cm):'))

luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)) 
volume = panjang * lebar * tinggi
keliling = 2 * (panjang + lebar + tinggi)

print('Luas Permukaan :',round(luas_permukaan))
print('Volume :',round(volume))
print('Keliling :',round(keliling))