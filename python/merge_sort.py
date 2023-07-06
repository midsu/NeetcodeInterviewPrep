'''
Divide: Find the midpoint of the list and ddivide into sublist
Conquare: Recursively sort the sublists created in previous step 
Combine: Merge the sorted sublist created in the previous step
'''

if len(list) <=1:
    return list

left_half, right_half = split(list)
left = merge_sort(left_half)
right = merge_sort(right_half)

return merge(left, right)