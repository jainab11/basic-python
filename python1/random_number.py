import random

# Generate a random list of numbers
length = 10
minimum = 1
maximum = 100
random_list = [random.randint(minimum, maximum) for _ in range(length)]

print("Random List:", random_list)

# Sort the random list using bubble sort
n = len(random_list)
for i in range(n):
    for j in range(0, n-i-1):
        if random_list[j] > random_list[j+1]:
            random_list[j], random_list[j+1] = random_list[j+1], random_list[j]

print("Sorted List:", random_list)
  