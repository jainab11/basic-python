def f_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
nums = [0,203,93]
result = f_largest(nums)
print(f"{result}")
            
    
# number = [1,2,4,4,64,34]
# largest = number[0]
# for num in number:
#     if num > largest:
#         largest = num
# print(largest)