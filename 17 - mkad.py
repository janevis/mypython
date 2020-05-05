v = int(input())
t = int(input())
route = v * t
lap = route // 109
mile = route - lap * 109
print(mile)
