year = int(input())
result = "NO"
if year % 4 == 0 and year % 100 != 0:
    result = "YES"
elif year % 400 == 0:
    result = "YES"
print(result)

i=0
for i in range (2020):
    if i % 4 == 0 and i % 100 == 0: print ("i1:", i)