import numpy as np
import string

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis = 0)

  
def split(word):
    return [i for i in word]

def punc_check(x):
    return True not in ([i in [i for i in string.punctuation] for i in x])

def letter_check(x):
    return False in ([i not in [i for i in string.ascii_lowercase] for i in x])

def number_check(x):
    return False not in ([i not in [str(i) for i in [*range(0, 9)]] for i in x])

def one_hot_2d(A, classes):
    return np.eye(classes)[:, A.reshape(-1)]

def one_hot_3d(A, classes):

    _, m, T = A.shape

    A_one_hot = np.zeros((classes, m, T))

    for t in range(T):
##        for i, j in enumerate(np.squeeze(A[:, :, t])):
##            A_one_hot[j, i, t] = 1
        A_one_hot[:, :, t] = one_hot_2d(A[:, :, t], classes)

    return A_one_hot
