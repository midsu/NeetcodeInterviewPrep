'''
Divide: Find the midpoint of the list and ddivide into sublist
Conquare: Recursively sort the sublists created in previous step 
Combine: Merge the sorted sublist created in the previous step
'''

''' if len(list) <= 1:
    return list

left_half, right_half = split(list)
left = merge_sort(left_half)
right = merge_sort(right_half)

return merge(left, right) '''

def split(list):
    '''
    Divide the unsorted list at midpoint into sublist
    Return 2 sublist - left and right
    '''
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

