# Write a function is_even that will return true if the passed-in number is even.

def is_even(integer):
    """checks if an integer is even, returns true if true, else false"""
    boolVal = True
    if integer % 2 != 0:
        boolVal = False

    return boolVal

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num):
    print("Even!")
else:
    print("Odd!")


