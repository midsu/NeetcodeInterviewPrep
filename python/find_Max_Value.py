def find_max(lst):
    if len(lst) == 0:
        return None
    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val

print(find_max([1, 5, 3, 8, 2])) # 8
print(find_max([])) # None
