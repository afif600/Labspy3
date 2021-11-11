from random import random
n = int(input("Masukan Nilai N: "))
for i in range(n):
    while True:
        n = random()
        if n < 0.5:
            break
    print("data ke:",(i+1), "=>",n)
print("Selesai")
