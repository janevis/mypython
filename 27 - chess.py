f = int(input())
h = int(input())
f1 = int(input())
h1 = int(input())
if f == f1 and h == h1:
    print("NO")
elif f - 2 < f1 < f + 2 and h - 2 < h1 < h + 2:
    print("YES")
else:
    print("NO")
