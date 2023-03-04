# ## Python3

# ### Introduction

# Say "Hello, World!" With Python
print("Hello, World!")


# Python If-Else
#!/bin/python3
N = int(input())
if((N%2 != 0) or (N >=6 and N <= 20)): print("Weird")
else: print("Not Weird")


# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print("{0} \n{1} \n{2}". format((a + b), max(a - b, b - a), (a * b)))


# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print("{0} \n{1}". format(a//b, a/b))


# Loops
if __name__ == '__main__':
    n = int(input())
[print(i**2) for i in range(n)]


# Write a function
def is_leap(year):
    leap = False   
    # Write your logic here
    if(year%4 == 0 and (year%100 != 0 or year%400 == 0)): leap = True   
    return leap
year = int(input())
print(is_leap(year))


# Print Function
if __name__ == '__main__':
    n = int(input())
print(*range(1, n+1), sep = "")
