numbers = list(map(float, input().split()))

matches = {}

while numbers:
    current_num = numbers[0]
    count = numbers.count(current_num)
    if current_num not in matches:
        matches[current_num] = count

    numbers = [x for x in numbers if x != current_num]

for num, value in matches.items():

    print(f"{num:.1f} - {value} times")
