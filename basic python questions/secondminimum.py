def seccond_mini(number):
    smallest = number[0]
    second_smallest = number[1]
    for num in number:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
        
    return second_smallest
num = [1,2,3,4]
result = seccond_mini(num)
print(result)