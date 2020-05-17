N = int(input())
i = 0
result = "NO"
while N >= 2**i:
    if N == 2**i:
        result = "YES"
    i = i + 1
print(result)
