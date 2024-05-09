lst = [5, 0, 0, 2, 9, 11, 0]
n = len(lst)
i = 0

for j in range(n):
    if lst[j] != 0:
        # Swap non-zero element with the element at index i
        lst[i], lst[j] = lst[j], lst[i]
        i += 1

# Fill the remaining positions with zeroes
while i < n:
    lst[i] = 0
    i += 1

print(lst)  



# new_lst =[]
# lst_1 =[]
# for i in range(n):
#     if lst[i] == 0:
#         new_lst.append(lst[i])
#     else:
#         lst_1.append(lst[i])
# new_lst = lst_1+new_lst
# print(new_lst)  