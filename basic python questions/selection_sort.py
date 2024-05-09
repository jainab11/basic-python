def selection_sort(num):
    n = len(num)
    for i in range(n-1):
        mini_inx = i
        for j in range(i+1,n):
            if num[mini_inx] > num[j]:
                num[mini_inx],num[j] = num[j],num[mini_inx]
    return num
listy = [52,45,63,21,12,35,11]
sorty = selection_sort(listy)
print(sorty)