def find_index(num,target):
    n = len(num)
    for i in range(0,n-1):
        if   target ==  num[i]+num[i+1]:
            return [i,i+1]
        # else:
        #     return 0
lst =[11,3,5,9,6,15]
target1 = 9
lst2 = [3,2,4]
target2 =6
print(find_index(lst,target1))
print(find_index(lst2,target2))
        
        