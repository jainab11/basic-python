lst = [1,2,3,4,5]
new_lst = []
mul =1
for i in range(len(lst)):
    mul = mul*lst[i]
    new_lst.append(mul)
print(new_lst)