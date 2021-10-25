hari = input("Masukkan hari : ")

# menggunakan percabangan
#if hari == "Senin" or "Selasa" or "Rabu" or "Kamis" or "Jumat" or "Sabtu" or "Minggu":
    #print("Valid")
#else:
    #print("Tidak Valid")


# menggunakan perulangan
hari_valid = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
for i in hari_valid:
    if hari == i:
        valid = True
        break
    else:
        valid = False
        break

if valid == True:
    print("Valid")
elif valid == False:
    print("Tidak valid")


