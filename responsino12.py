#volume silinder
def luas_alas(r):
    return  3.14 * r ** 2
def VolumeSilinder(r,t):
    return  luas_alas(r) * t


r = int(input())
t = int(input())
print(VolumeSilinder(r,t))