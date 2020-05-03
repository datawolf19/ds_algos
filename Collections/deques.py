from collections import deque

dq = deque('abc') # creates deque

dq.append('d') # adds value to the right

dq.appendleft('z') # adds value to the left

dq.extend('efg') # adds multiple items to the right

dq.extendleft('yxw') # adds multiple items to the left

print(dq)

dq.pop() # removes 'g' from right

dq.popleft() # removes item from left

print(dq)

