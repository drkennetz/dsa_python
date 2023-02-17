# Why Recursion?
- recursive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use
    - when to use recursion?
        - if you can divide the problem into smaller sub problems
        - design an algorithm to compute nth
        - write code to list the n
        - implement a method to compute all
        - practice
- The prominent usage of recursion in data structures like trees and graphs
- Interviews
- It is used in many algorithms (divide and conquer, greedy, and dynamic programming)

# How recursion works?
1. A method calls itself
2. Exit from infinte loop

```python
def firstMethod():
    secondMethod()
    print("I am the first method")

def secondMethod():
    thirdMethod()
    print("I am the second method")

def thirdMethod():
    fourthMethod()
    print("I am the third method")

def fourthMethod():
    print("I am the fourth method")
```

## STACK MEMORY FOR ABOVE
****************
xxxxxxxxxxxx
****************
xxxxxxxxxx
**********************************
thirdMethod()
**********************
secondMethod()
**********************
firstMethod()

- Firsth method calls second method which calls third method which calls fourth method.
- computer puts first method on stack, then second method, then third method
- fourth method doesn't call any other methods so it doesn't get put on stack, it gets executed
- Now, computer works its way through stack through LIFO

## Now with recursion
```python
def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)
```
- lets use an example of 4 as starting input on stack
**********
executes
**********
recursiveMethod(1)
**********
recursiveMethod(2)
**********
recursiveMethod(3)
**********
recursiveMethod(4)

- recursive method puts subsequent calls on stack until base condition is satisfied

# Recursive vs Iterative Solutions
- all recursive functions can be implemented iteratively, although sometimes it is much more complex to do it
```python
# recursion
def pow2(n):
    if n == 0:
        return 1
    else:
        power = pow2(n-1)
        return power * 2

# iteration
def pow2(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power
```
### differences
- recursive is easier to write (this is simple, so may not notice here)
- conditional statement decides termination in recursion, comparison decides in iterator
- infinite recursion leads to system crash, infinite iteration consumes cpu cycles
- recursion repeatedly invokes mechanism with overhead of method calls, which can be expensive in both processor time and memory space, iteration does not
- recursive functions can be very space inefficient

So should we always use iteration? No.
- use recursion when a problem can be divided into similar subproblems
- in data structures like trees and graphs, recursion is more efficient

### table

| Points | recursion | iteration | Description |
|-----| --- | --- | --- |
| Space Efficient? | No | Yes |  No stack memory required in case of iteration
| Time Efficient? |No | Yes | In case of recursion system needs more time for pop and push elements to stack memory which makes recursion less time efficient
| Easy to Code? | Yes | No | We use recursion especially in cases we know that a problem can be divided into similar sub problems 

# When to use / avoid recursion?
When to use it?
- when we can easily break a problem into similar subproblem
- when we are fine with extra overhead (both space and time) that comes with it
- when we need a quick solution instead of efficient one
- when traverse a tree
    - preorder traversal
- when we use memoization in recursion

When to avoid it?
- if time and space complexity matters for our application
- recursion uses more memory. if we use embedded memory. For example, an application that takes more memory in the phone is not efficient
- Can be slow

