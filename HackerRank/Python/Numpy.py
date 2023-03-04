# Arrays
import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    #return numpy.array(arr[::-1], dtype = float) #Another Solution
    return numpy.flip(numpy.array(arr, float), 0)
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# Shape and Reshape
import numpy as np
print(np.array(input().split(), int).reshape(3, 3))


# Transpose and Flatten
import numpy as np
N, M = map(int, input().split())
arr = []
arr = np.array([input().strip().split() for _ in range(N)], int)
print(np.transpose(arr))
print(arr.flatten())


# Concatenate
import numpy as np
# print(np.array([input().split(' ') for _ in range( np.array(input().split(' '), int)[:-1].sum() )], int)) #Another Solution
n, m, p = map(int, input().split())
a = np.array([input().split() for _ in range(n)], dtype = int)
b = np.array([input().split() for _ in range(m)], dtype = int)
print(np.concatenate((a, b)))


# Zeros and Ones
import numpy as np
n = tuple(map(int, input().split()))
print(np.zeros(n, dtype = np.int))
print(np.ones(n, dtype = np.int))


# Eye and Identity
import numpy as np
#n, m = map(int, input().split())
np.set_printoptions(sign=' ')
print(np.eye(*map(int, input().split())))


# Array Mathematics
import numpy as np
N, M = map(int, input().split())
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)
print(np.add(A, B), np.subtract(A, B), np.multiply(A, B), np.floor_divide(A, B), np.mod(A, B), np.power(A, B), sep = '\n')


# Floor, Ceil and Rint
import numpy as np
A = np.array(input().split(), float)
np.set_printoptions(sign = ' ')
print(np.floor(A), np.ceil(A), np.rint(A), sep = '\n')


# Sum and Prod
import numpy as np
# print( np.product( np.sum( [ np.array(input().split(), int) for _ in range(int(input().split(' ')[0])) ], axis = 0 ) ) ) #Another Solution
N, M = map(int, input().split())
A = np.array([input().split() for _ in range(N)], dtype = int)
print(np.product(np.sum(A, axis = 0)))


# Min and Max
import numpy as np
N, M = map(int, input().split())
A = np.array([input().split() for _ in range(N)], int)
print (np.max(np.min(A, axis = 1)))


# Mean, Var, and Std
import numpy as np
np.set_printoptions(legacy='1.13')
N, M = map(int, input().split())
A = np.array([input().split() for i in range(N)], dtype = int)
print(np.mean(A, axis = 1), np.var(A, axis = 0), np.std(A), sep = '\n')


# Dot and Cross
import numpy as np
#np.set_printoptions(legacy='1.13')
N = int(input())
A = np.array([input().split() for i in range(N)], dtype = int)
B = np.array([input().split() for i in range(N)], dtype = int)
print(np.dot(A, B))


# Inner and Outer
import numpy as np
#np.set_printoptions(legacy='1.13')
A = np.array(input().split(), dtype = int)
B = np.array(input().split(), dtype = int)
print(np.inner(A, B), np.outer(A, B), sep = '\n')


# Polynomials
import numpy
print(numpy.polyval(list(map(float, input().split())), float(input())))


# Linear Algebra
import numpy as np
N = int(input())
A = np.array([input().split() for _ in range(N)], float)
print(round(np.linalg.det(A), 2))
