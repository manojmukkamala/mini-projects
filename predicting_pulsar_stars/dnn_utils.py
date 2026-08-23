
# coding: utf-8

# ### Required Functions
# 
# In this notebook, we are going to build the functions required by the Neural Network

# 1. Sigmoid Activation Function

# In[5]:


import numpy as np


# In[1]:


def sigmoid(Z):
    """
    Implements the sigmoid activation in numpy
    
    Arguments:
    Z -- numpy array of any shape
    
    Returns:
    A -- output of sigmoid(z), same shape as Z
    cache -- returns Z as well, useful during backpropagation
    """
    A = 1.0/(1.0 + np.exp(-Z))
    assert(A.shape == Z.shape)
    cache = Z
    
    return A, cache


# 2.2 RELU Activation Function

# In[2]:


def relu(Z):
    """
    Implement the RELU function.

    Arguments:
    Z -- Output of the linear layer, of any shape

    Returns:
    A -- Post-activation parameter, of the same shape as Z
    cache -- a python dictionary containing "A" ; stored for computing the backward pass efficiently
    """
    A = np.maximum(0, Z)
    assert(A.shape == Z.shape)
    
    cache = Z
    return A, cache


# 2.3 Derivative of Sigmoid function

# In[3]:


def sigmoid_backward(dA, cache):
    """
    Implement the derivative for sigmoid function.

    Arguments:
    dA -- post-activation gradient for current layer l 
    cache -- activation_cache we store for computing backward propagation efficiently

    Returns:
    dZ -- Gradient of the cost with respect to the linear output (of current layer l)
    """
    Z = cache
    s = 1.0/(1.0 + np.exp(-Z))
    dZ = dA * s * (1 - s)
    
    assert(dZ.shape == Z.shape)
    return dZ


# 2.4 Derivative of Relu function

# In[4]:


def relu_backward(dA, cache):
    """
    Implement the derivative for relu function.

    Arguments:
    dA -- post-activation gradient for current layer l 
    cache -- activation_cache we store for computing backward propagation efficiently

    Returns:
    dZ -- Gradient of the cost with respect to the linear output (of current layer l)
    """  
    Z = cache
    dZ = np.array(dA, copy = True)
    dZ[Z <= 0] = 0
    
    assert(dZ.shape == Z.shape)
    return dZ

