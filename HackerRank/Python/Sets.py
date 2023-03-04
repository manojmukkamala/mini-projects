# Introduction to Sets
def average(array):
    # your code goes here
    return (sum(set(array))/(len(set(array))))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# No Idea!
n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
print (sum([(i in a) - (i in b) for i in arr]))


# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
print(len(set(input() for _ in range(n))))


# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    c = input()
    if c == 'pop':
        s.pop()
    else:
        cmd, val = c.split()
        #print(cmd, val)
        cmd = 's.'+cmd+'('+str(val)+')'
        eval(cmd)
print(sum([i for i in s]))


# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e|f))


# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e&f))


# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e-f))


# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e^f))


# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, l = input().split()
    B = set(map(int, input().split()))
    eval("A." + cmd + "(B)")
print(sum(A))


# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*n) - sum(arr))//(n - 1))


# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
    
   
# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
print(all(a > set(map(int, input().split())) for _ in range(int(input()))))
