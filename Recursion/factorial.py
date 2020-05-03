# Recursion is a 'divide and conquer' problem.
# There are two cases: 1. base cases that tell the recursive function to end and 
# 2. recursive cases that call the function repeatedly. 

# Factorial Problem
# Base case: when n is 0
# Recursive case: when n > 0

def factorial(n):
    # test for base case
    if n==0:
        return 1

    # calculate and call factorial again
    f = n * factorial(n-1)
    print(f)
    return f

factorial(4)

# Iterations offer more control but recursion models mathematical concepts.
# Additionally, recursive calls are stored in memory. Iterations are not.
# Tradeoff: Processor cycles vs Memory Usage