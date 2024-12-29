d = {'A': 10, 'B': 20, 'C': 30, 'D': 10, 'E': 10, 'F': 20, 'G': 30}
dt = {}

for key, value in d.items():
    if value not in dt:
        dt[value] = {key}
    else:
        dt[value].add(key)

print(dt)
