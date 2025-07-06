def factorials (x):
    '''This is a recursive function to find the factorial of a integer'''

    if x == 0 or x == 1:
        return 1
    else:
        return x*factorials(x-1)
    

print(factorials.__doc__)
print("The factorial of 0 is", factorials(0))
print("The factorial of 1 is", factorials(1))
print("The factorial of 3 is", factorials(3))
print("The factorial of 5 is", factorials(5))
print("The factorial of 10 is",factorials(10))