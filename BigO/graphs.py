import matplotlib.pyplot as plt
import math

asymptotic = """When evaluating an algorithm's runtime performance
consider the following:
1. Worst case - use an input that gives the slowest performance
2. Best case - use an input thath gives the best results
3. Avg case - assume random input
"""

x = list(range(1,100))
l=[]; l2=[]; a=1
plt.plot(x, [y*y for y in x], label='x^2')

# These 7 & 6 item plots are in the same complexity class.
plt.plot(x, [(7 * y) * math.log(y,2) for y in x], label='7 ops')
plt.plot(x, [(6*y) * math.log(y,2) for y in x], label='6 ops')
plt.xlabel("n - size")
plt.ylabel("t - time")
plt.legend()
print(asymptotic)
plt.show()

