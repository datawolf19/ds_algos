# Iteration example:
def iterTest(low, high):
    while low <= high:
        print(low)
        low+=1

# Recursion example:
def recurTest(low, high):
    if low<=high:
        print(low)
        recurTest(low+1, high)

# Takeaway:
# Generally, iteration is more efficient but recursive functions can be 
# easier to understand. Useful for linked lists and trees data structures.

if __name__ == "__main__":
    iterTest(1, 10)

    recurTest(11,20)