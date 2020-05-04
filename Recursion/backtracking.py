# Backtracking
# Useful for traversing tree structures
# Nodes have options. Choose one option.
# More options appear. Depending on the
# choices made you reach a goal state or
# dead end. If you reach a dead end you 
# go back one node and explore each branch.

# Backtracking is a divide and conquer method
# for an exhaustive search. It also prunes
# branches that can't give results.

def bitStr(n, s):
    """Generate all permutations of a string s 
    given a length n.

    Order matters for a permutation. Of n things 
    taken 'r' at a time."""

    
    if n==1: return s # base case

    return [digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1, s)]

print(bitStr(3, 'abc'))