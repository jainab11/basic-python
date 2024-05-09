# perfect number is a number whoes factors are eqal to that no.
num = 9
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum = sum+i
if sum == num:
    print("number is perfect number")
else:
    print("number is not a perfect number")