def kpk(bil1, bil2):
    # Mencari faktor persekutuan terbesar (FPB)
    def fpb(a, b):
        while b:
            a, b = b, a % b
        return a

    # Menghitung KPK menggunakan rumus KPK = (a * b) / FPB(a, b)
    return (bil1 * bil2) // fpb(bil1, bil2)

# Contoh penggunaan
a = int(input("masukan angka 1 : "))
b = int(input("Masukan angka 2 :"))
hasil = kpk(a, b)
print("Hasil KPK:", hasil)

