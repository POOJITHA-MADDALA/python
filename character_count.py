s = "welcome to python class"
char_count = {}

for char in s:
    if char != ' ':  # Ignore spaces
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
print(char_count)
