N = int(input())
i = 0
string = ''
while N >= 2**i:
    string = string + str(2**i) + " "
    i = i + 1
print(string)
