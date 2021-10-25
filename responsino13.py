#bilangan prima
def CekPrima(x):
    jumlah_faktor = 0
    i = 1
    while (i <= x):
        if (x%i == 0):
            jumlah_faktor += 1
        i+=1
    #CEK JUMLAH FAKTORNYA PRIMA ATAU BUKAN
    if jumlah_faktor == 2:
        prima = True
    else:
        prima = False
    return prima


angka = int(input())
if CekPrima(angka) == True:
    print(angka, "adalah prima")
else:
    print(angka,"bukan prima")