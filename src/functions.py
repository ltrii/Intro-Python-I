# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num):
    numcheck = num % 2
    if numcheck == 0:
        return True
    else:
        return False

print(is_even(10))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if is_even(num) == False:
    print("Odd")
else:
    print("Even!")


