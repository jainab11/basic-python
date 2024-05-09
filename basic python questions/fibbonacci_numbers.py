# n1 = 0
# n2 = 1
# count =0
# for i in range(1 ,10):
#     nth = n1+n2
#     n1 = n2
#     n2 = nth
#     count +=1
#     print(n1 , end =" ")
    
    
    #  addition of list like fibbonacci numbers
lst = [1, 24, 6, 3, 43, 53]
n1, n2 = lst[0], lst[1]
count = 0
n = len(lst)
fibo_list = []

for i in range(n):
    fibo_list.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth

for j in fibo_list:
    count += lst[i]
print(fibo_list)


