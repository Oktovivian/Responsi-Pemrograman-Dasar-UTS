n = int(input("Masukkan n: "))
# pakai for range
# n=5
for i in range(1,n+1):          #range(1,6)
    for j in range(1,i+1):      #range(1,6)
        print("*",end="")
    print() #pindah baris

for i in range(n-1,0,-1):
    for j in range(1,i+1,1):
        print("*",end="")
    print() #pindah baris
