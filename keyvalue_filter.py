d = {'A': 10, 'B': 20}
l = [10, 20, 30]

output_set = set()

for key, value in d.items():
    if value in l:
        output_set.add((key, value))

print(output_set)

print("test line from linux server")
