total_belanja = float(input("Masukan Total Belanja: Rp "))

# Aturan Diskon
if(total_belanja >= 50000 and total_belanja < 100000):
	diskon = 0.05 # 5%
elif(total_belanja >= 100000 and total_belanja <= 500000):
	diskon = 0.1 # 10%
elif(total_belanja > 500000):
	diskon = 0.25 # 25%
else:
	diskon = 0 # 0%

# Hitung Jumlah diskon
jumlah_diskon = total_belanja * diskon

# Hitung Total Pembayaran
total_pembayaran = total_belanja - jumlah_diskon

print(f"Total Pembayaran setelah diskon: Rp {total_pembayaran:.2f}")

