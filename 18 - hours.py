N = int(input())
h = N // 3600
m = N - h * 3600
m1 = m // 60
s = N - (h * 3600 + m1 *60)
print(h ,":", m1 , ":", s)