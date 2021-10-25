total_belanja = int(input("Masukkan total belanja: "))
is_member = input("Apakah member (Ya/Tidak): ")

if (total_belanja>=5000 and total_belanja<=1000000):
    diskon = 2
elif (total_belanja > 1000000):
    diskon = 3
else:
    diskon = 0

if (is_member == 'Ya'):
    diskon = diskon + 5

print("Anda mendapatkan diskon {}%%".format(diskon))
