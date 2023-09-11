jumlah_data = int(input("Enter your jumlah data: "))
total = 0

for s in range(jumlah_data):
    data = int(input("Masukkan data ke-{}: ".format(s + 1)))
    total += data

if jumlah_data > 0:
    rata_rata = total / jumlah_data
    print("Rata-rata =", rata_rata)
else:
    print("Nothing")

