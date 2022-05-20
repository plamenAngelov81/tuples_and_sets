n = int(input())

unique_names = set()

for i in range(n):
    name = input()
    unique_names.add(name)

[print(x) for x in unique_names]
