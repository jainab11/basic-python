def reverse_list_location(lst, start_pos, end_pos):
    while start_pos < end_pos:
        lst[start_pos], lst[end_pos] = lst[end_pos], lst[start_pos]
        start_pos += 1
        end_pos -= 1
    return lst
nums = [10,20,30,40,50,67,85,34,24]
end = 8
start = 1
result = reverse_list_location(nums,start,end)
print(result)
