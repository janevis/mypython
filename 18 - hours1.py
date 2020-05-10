N = int(input())
d = N // 86400
h = (N - d * 86400) // 3600
m = (N - d * 86400) - h * 3600
m1 = m // 60
s = (N - d * 86400) - (h * 3600 + m1 * 60)
print(h, ":", "{:02d}".format(m1), ":", "{:02d}".format(s), sep="")
