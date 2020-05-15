a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("3")
elif b != a == c or b == a != c or c != b == a or a != b == c:
    print("2")
elif (a != b) and (a != c) and (c != b):
    print(0)
