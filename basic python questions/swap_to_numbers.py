def swap_numbers(x, y):
    # x = x ^ y
    # y = x ^ y
    # x = x ^ y
    # x = x + y
    # y = x - y
    # x = x - y
    temp = x
    x = y
    y = temp
    
    return x, y
num1 =9
num2 = 10
print(f"befor swapping  number is  {num1}, {num2} ")
swapii = swap_numbers(num1,num2)
print(swapii)