# def check_prime(num):
#     if num < 2:
#         return False
#     for i in range (2 , int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     else:
#         return True
    
# number = 5
# result = check_prime(number)
# print(result)
num1 = 10
for i in range(2 ,num1):
    if num1 % i == 0:
        print("not a prime")
        break
else:
    print("prime")