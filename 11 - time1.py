N = int(input())
if N >= 1440:
    days = N // 1440
    N = N - days * 1440
hours = N // 60
minutes = N - hours * 60
print(hours, minutes)
