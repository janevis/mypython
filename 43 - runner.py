X = int(input())
Y = int(input())
i = 1
while Y > X:
    X = X + X * 0.1
    i += 1
print(i)
