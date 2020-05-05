N = 3800
h = N // 3600
m = N - h * 3600
m1 = m // 60
s = N - (h * 3600 + m1 *60)
#print(h ,":", m1 , ":", s)
print("{:02d}".format(h),":","{:02d}".format(m1),":", "{:02d}".format(s), sep="")
