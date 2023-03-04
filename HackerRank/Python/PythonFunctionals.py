#Map and Lambda Function 

cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    
    #f = [0, 1]
    #[f.append(sum(f[-2:])) for i in range(n-2)]
    #return [] if n == 0 else [0] if n == 1 else f 
    
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i-2] + a[i-1])
    return a[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))



#Validating Email Addresses With a Filter

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False
    
    if username.replace("-", "").replace("_", "").isalnum() is False or len(username) == 0:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3 or len(extension) == 0:
        return False
    else:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


#Reduce Function

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
