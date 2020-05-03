A = int(input())
B = int(input())
N = int(input())
A1 = A * 100
B1 = A1 + B
B2 = B1 * N
rubles = B2 // 100
kopeeks = B2 - rubles * 100
print(rubles, kopeeks)
