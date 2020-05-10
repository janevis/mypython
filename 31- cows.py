n = int(input())
m = n // 10
if 0 <= (n - 10) < 10:
    print(n, "korov")
elif n == 9 or (n - m*10) == 9:
    print(n, "korov")
elif n == 8 or (n - m*10) == 8:
    print(n, "korov")
elif n == 7 or (n - m*10) == 7:
    print(n, "korov")
elif n == 6 or (n - m*10) == 6:
    print(n, "korov")
elif n == 5 or (n - m*10) == 5:
    print(n, "korov")
elif n == 4 or (n - m*10) == 4:
    print(n, "korovy")
elif n == 3 or (n - m*10) == 3:
    print(n, "korovy")
elif n == 2 or (n - m*10) == 2:
    print(n, "korovy")
elif n == 1 or (n - m*10) == 1:
    print(n, "korova")
elif n % 10 == 0:
    print(n, "korov")
