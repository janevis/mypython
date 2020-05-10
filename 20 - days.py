N = int(input())
M = int(input())
days = M // N
if M % N != 0:
    days += 1
print(days)
