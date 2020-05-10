A = int(input())
B = int(input())
C = int(input())
if B <= A >= C:
    print(A)
elif A <= B >= C:
    print(B)
elif A <= C >= B:
    print(C)
