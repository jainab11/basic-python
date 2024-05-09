def remove_duplicates(num):
    unique_element = []
    for i in num:
        if i not in unique_element:
            unique_element.append(i)
    return unique_element
list1 = [1,2,4,2,3,5,6,3]
uniques = remove_duplicates(list1)
print(uniques)