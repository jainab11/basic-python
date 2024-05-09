lst =[2,9,20,31,45]
ans_lst = []
n = len(lst)
for i in range(0,n):
    ans_lst.append(lst[i])
    lst[i] = lst[i]+lst[i+1]
print(ans_lst)   