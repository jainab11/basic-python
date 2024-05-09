def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
num = 5
if check_prime(num):
    print(f" The given number {num} is prime")
else:
    print(f" Given number  {num} is not a prime number")
# result = check_prime(num)
# print(f" The entered number is {result}")
# Taking input from the user for the range
"""start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            """
