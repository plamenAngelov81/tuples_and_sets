numbers = [int(x) for x in input().split()]
target = int(input())

unique_tuples = set()

counter = 0
for i in range(len(numbers)):
    for j in range((i + 1), len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")
            num_tuple = (numbers[i], numbers[j])
            unique_tuples.add(num_tuple)
        counter += 1

print(f"Iterations done: {counter}")
[print(unique) for unique in unique_tuples]
