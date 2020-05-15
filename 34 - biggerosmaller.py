a, b, c = int(input()), int(input()), int(input())
if b <= a <= c:
    (a, b) = (b, a)
elif b <= c <= a:
    (a, b) = (b, a)
    (b, c) = (c, b)
elif c <= a <= b:
    (a, c) = (c, a)
    (b, c) = (c, b)
elif c <= b <= a:
    (c, a) = (a, c)
elif a <= c <= b:
    (b, c) = (c, b)
print(a, b, c)
