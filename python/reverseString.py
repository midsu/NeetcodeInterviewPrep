def reverse_string(s):
    result = ""
    for c in s:
        result = c + result
    return result

print(reverse_string("hello")) # "olleh"
print(reverse_string("")) # ""
