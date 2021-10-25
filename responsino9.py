n = int(input("Masukkan n: "))
# pakai for range
# n=5
#for i in range(1,n+1):          #range(1,6)
    #for j in range(1,n+1):      #range(1,6)
        #print(j,end="")
    #print() #pindah baris

# pakai while
i = 1
while (i<=n):
    j = 1
    while (j<=n):
        print(j,end="")
        j += 1
    print()
    i += 1