# ### Basic Data Types

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if((i + j + k)!= n)])


# Find the Runner-Up Score! 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])


# Nested Lists
if __name__ == '__main__':
    n = int(input())
    arr = [[input(), float(input())] for _ in range(n)]
    c = sorted(set([b for a, b in arr]))[1]
    print('\n'.join(sorted(a for a, b in arr if b == c)))


# Finding the Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('%.2f' %(sum(student_marks[query_name])/len(student_marks[query_name])))


# Lists
if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if (cmd != 'print'):
            cmd += "("+",".join(args) +")"
            eval("l."+cmd)
        else:
            print (l)


# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
