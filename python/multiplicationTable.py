# Print the multiplication table for a number using a while loop

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1
