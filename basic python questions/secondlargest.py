def find_seccond_largest(number):
    second_maxi = number[0]
    maxi = number[1]
    for  num in number:
        if num > maxi:
            second_maxi = maxi
            maxi = num
        elif num > second_maxi and num != maxi:
            second_maxi = num
            
    return second_maxi
num = [1,2,3,4, 8]
result = find_seccond_largest(num)
print(result)