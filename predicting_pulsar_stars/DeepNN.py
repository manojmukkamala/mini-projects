
# coding: utf-8

# ### Deep Neural Network
# 
# In this notebook, we will build a deep neural network, with as many layers as we want.

# ### 1 - Packages
# Let's first import all the packages that we will need during the task.
# 
# - [numpy](www.numpy.org) is the main package for scientific computing with Python.
# - [matplotlib](http://matplotlib.org) is a library to plot graphs in Python.
# - np.random.seed(1) is used to keep all the random function calls consistent.

# In[1]:


import numpy as np
from dnn_utils import *
import matplotlib.pyplot as plt


# ## Outline
# 
# 
# - Initialize the parameters for an $L$-layer neural network.
# - Implement the forward propagation module 
# - Compute the loss.
# - Implement the backward propagation module
# - Finally update the parameters.

# ### 2 - Initialize Parameters
# 
# 
# The initialization for a deeper L-layer neural network is more complicated because there are many more weight matrices and bias vectors. When completing the `initialize_parameters_deep`, you should make sure that your dimensions match between each layer. Recall that $n^{[l]}$ is the number of units in layer $l$. Thus for example if the size of our input $X$ is $(12288, 209)$ (with $m=209$ examples) then:
# 
# <table style="width:100%">
# 
# 
#     <tr>
#         <td>  </td> 
#         <td> **Shape of W** </td> 
#         <td> **Shape of b**  </td> 
#         <td> **Activation** </td>
#         <td> **Shape of Activation** </td> 
#     <tr>
#     
#     <tr>
#         <td> **Layer 1** </td> 
#         <td> $(n^{[1]},12288)$ </td> 
#         <td> $(n^{[1]},1)$ </td> 
#         <td> $Z^{[1]} = W^{[1]}  X + b^{[1]} $ </td> 
#         
#         <td> $(n^{[1]},209)$ </td> 
#     <tr>
#     
#     <tr>
#         <td> **Layer 2** </td> 
#         <td> $(n^{[2]}, n^{[1]})$  </td> 
#         <td> $(n^{[2]},1)$ </td> 
#         <td>$Z^{[2]} = W^{[2]} A^{[1]} + b^{[2]}$ </td> 
#         <td> $(n^{[2]}, 209)$ </td> 
#     <tr>
#    
#        <tr>
#         <td> $\vdots$ </td> 
#         <td> $\vdots$  </td> 
#         <td> $\vdots$  </td> 
#         <td> $\vdots$</td> 
#         <td> $\vdots$  </td> 
#     <tr>
#     
#    <tr>
#         <td> **Layer L-1** </td> 
#         <td> $(n^{[L-1]}, n^{[L-2]})$ </td> 
#         <td> $(n^{[L-1]}, 1)$  </td> 
#         <td>$Z^{[L-1]} =  W^{[L-1]} A^{[L-2]} + b^{[L-1]}$ </td> 
#         <td> $(n^{[L-1]}, 209)$ </td> 
#     <tr>
#     
#     
#    <tr>
#         <td> **Layer L** </td> 
#         <td> $(n^{[L]}, n^{[L-1]})$ </td> 
#         <td> $(n^{[L]}, 1)$ </td>
#         <td> $Z^{[L]} =  W^{[L]} A^{[L-1]} + b^{[L]}$</td>
#         <td> $(n^{[L]}, 209)$  </td> 
#     <tr>
# 
# </table>
# 
# Remember that when we compute $W X + b$ in python, it carries out broadcasting. For example, if: 
# 
# $$ W = \begin{bmatrix}
#     j  & k  & l\\
#     m  & n & o \\
#     p  & q & r 
# \end{bmatrix}\;\;\; X = \begin{bmatrix}
#     a  & b  & c\\
#     d  & e & f \\
#     g  & h & i 
# \end{bmatrix} \;\;\; b =\begin{bmatrix}
#     s  \\
#     t  \\
#     u
# \end{bmatrix} $$
# 
# Then $WX + b$ will be:
# 
# $$ WX + b = \begin{bmatrix}
#     (ja + kd + lg) + s  & (jb + ke + lh) + s  & (jc + kf + li)+ s\\
#     (ma + nd + og) + t & (mb + ne + oh) + t & (mc + nf + oi) + t\\
#     (pa + qd + rg) + u & (pb + qe + rh) + u & (pc + qf + ri)+ u
# \end{bmatrix}  $$

# In[2]:


def initialize_parameters(layer_dims):
    """
    Arguments:
    layer_dims -- python array (list) containing the dimensions of each layer in our network
    
    Returns:
    parameters -- python dictionary containing your parameters "W1", "b1", ..., "WL", "bL":
                    Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])
                    bl -- bias vector of shape (layer_dims[l], 1)
    """
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)    # number of layers in the network
    
    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1])
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
        
        assert(parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l-1]))
        assert(parameters['b' + str(l)].shape == (layer_dims[l], 1))
        
        
    return parameters
        


# ### 3 - Forward Propagation module

# #### 3.1 - Linear Forward
# 
# The linear forward module (vectorized over all the examples) computes the following equations:
# 
# $$Z^{[l]} = W^{[l]}A^{[l-1]} +b^{[l]}$$
# 
# where $A^{[0]} = X$. 

# In[3]:


def linear_forward(A, W, b):
    """
    Implement the linear part of a layer's forward propagation.

    Arguments:
    A -- activations from previous layer (or input data): (size of previous layer, number of examples)
    W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)
    b -- bias vector, numpy array of shape (size of the current layer, 1)

    Returns:
    Z -- the input of the activation function, also called pre-activation parameter 
    cache -- a python dictionary containing "A", "W" and "b" ; stored for computing the backward pass efficiently
    """
    
    Z = np.dot(W, A) + b
    
    assert(Z.shape == (W.shape[0], A.shape[1]))
    cache = [A, W, b]
    
    return Z, cache


# #### 3.2 - Linear Activation Forward
# 
# In this notebook, we will use two activation functions:
# 
# - **Sigmoid**: $\sigma(Z) = \sigma(W A + b) = \frac{1}{ 1 + e^{-(W A + b)}}$. We have provided you with the `sigmoid` function. This function returns **two** items: the activation value "`a`" and a "`cache`" that contains "`Z`" (it's what we will feed in to the corresponding backward function). To use it you could just call: 
# ``` python
# A, activation_cache = sigmoid(Z)
# ```
# 
# - **ReLU**: The mathematical formula for ReLu is $A = RELU(Z) = max(0, Z)$. We have provided you with the `relu` function. This function returns **two** items: the activation value "`A`" and a "`cache`" that contains "`Z`" (it's what we will feed in to the corresponding backward function). To use it you could just call:
# ``` python
# A, activation_cache = relu(Z)
# ```

# In[4]:


def linear_activation_forward(A_prev, W, b, activation):
    """
    Implement the forward propagation for the LINEAR->ACTIVATION layer

    Arguments:
    A_prev -- activations from previous layer (or input data): (size of previous layer, number of examples)
    W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)
    b -- bias vector, numpy array of shape (size of the current layer, 1)
    activation -- the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"

    Returns:
    A -- the output of the activation function, also called the post-activation value 
    cache -- a python dictionary containing "linear_cache" and "activation_cache";
             stored for computing the backward pass efficiently
    """
    
    if activation == 'sigmoid':
        # Inputs: A_prev, W, b. Outputs: A, activation_cache
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = sigmoid(Z)
        
    elif activation == 'relu':
        # Inputs: A_prev, W, b. Outputs: A, activation_cache
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = relu(Z)
        
    assert (A.shape == (W.shape[0], A_prev.shape[1]))
    cache = (linear_cache, activation_cache)
    
    return A, cache


# #### 3.3 - L Layer Model
# 
# For even more convenience when implementing the $L$-layer Neural Net, we will need a function that replicates the previous one (`linear_activation_forward` with RELU) $L-1$ times, then follows that with one `linear_activation_forward` with SIGMOID.
# 
# 
# 
# In the code below, the variable `AL` will denote $A^{[L]} = \sigma(Z^{[L]}) = \sigma(W^{[L]} A^{[L-1]} + b^{[L]})$. (This is sometimes also called `Yhat`, i.e., this is $\hat{Y}$.) 

# In[5]:


def L_model_forward(X, parameters):
    """
        Arguments:
    X -- data, numpy array of shape (input size, number of examples)
    parameters -- output of initialize_parameters_deep()
    
    Returns:
    AL -- last post-activation value
    caches -- list of caches containing:
                every cache of linear_activation_forward() (there are L-1 of them, indexed from 0 to L-1)
    """
    caches = []
    A = X
    L = len(parameters) // 2     # number of layers in the neural network
    
    # Implement [LINEAR -> RELU]*(L-1). Add "cache" to the "caches" list.
    for l in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)], activation = 'relu')
        caches.append(cache)
    
    # Implement LINEAR -> SIGMOID. Add "cache" to the "caches" list.
    AL, cache = linear_activation_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], activation = 'sigmoid')
    caches.append(cache)
    
    assert(AL.shape == (1, X.shape[1]))
    
    return AL, caches


# ### 4 - Cost Function

# Now let's implement backward propagation. We need to compute the cost, because you want to check if your model is actually learning.
# 
# Compute the cross-entropy cost $J$, using the following formula: $$-\frac{1}{m} \sum\limits_{i = 1}^{m} (y^{(i)}\log\left(a^{[L] (i)}\right) + (1-y^{(i)})\log\left(1- a^{[L](i)}\right)) $$

# In[6]:


def compute_cost(AL, Y):
    """
    Implement the cost function defined by above equation.

    Arguments:
    AL -- probability vector corresponding to your label predictions, shape (1, number of examples)
    Y -- true "label" vector (for example: containing 0 if non-cat, 1 if cat), shape (1, number of examples)

    Returns:
    cost -- cross-entropy cost
    """
    
    m = Y.shape[1]
    
    # Compute loss from aL and y.
    cost = (-1/float(m)) * (np.dot(Y, np.transpose(np.log(AL))) + np.dot((1 - Y), np.transpose(np.log(1 - AL))))
    
    cost = np.squeeze(cost) # To make sure the cost's shape is what we expect (e.g. this turns [[17]] into 17).
    assert(cost.shape == ())
    
    return cost


# ### 5.Backward Propagation

# Just like with forward propagation, we will implement helper functions for backpropagation. Remember that back propagation is used to calculate the gradient of the loss function with respect to the parameters.

# #### 5.1 - Linear Backward
# 
# For layer $l$, the linear part is: $Z^{[l]} = W^{[l]} A^{[l-1]} + b^{[l]}$ (followed by an activation).
# 
# Suppose you have already calculated the derivative $dZ^{[l]} = \frac{\partial \mathcal{L} }{\partial Z^{[l]}}$. You want to get $(dW^{[l]}, db^{[l]} dA^{[l-1]})$.
# 
# The three outputs $(dW^{[l]}, db^{[l]}, dA^{[l]})$ are computed using the input $dZ^{[l]}$.Here are the formulas you need:
# $$ dW^{[l]} = \frac{\partial \mathcal{L} }{\partial W^{[l]}} = \frac{1}{m} dZ^{[l]} A^{[l-1] T} $$
# $$ db^{[l]} = \frac{\partial \mathcal{L} }{\partial b^{[l]}} = \frac{1}{m} \sum_{i = 1}^{m} dZ^{[l](i)} $$
# $$ dA^{[l-1]} = \frac{\partial \mathcal{L} }{\partial A^{[l-1]}} = W^{[l] T} dZ^{[l]} $$

# In[7]:


def linear_backward(dZ, cache):
    """
    Implement the linear portion of backward propagation for a single layer (layer l)

    Arguments:
    dZ -- Gradient of the cost with respect to the linear output (of current layer l)
    cache -- tuple of values (A_prev, W, b) coming from the forward propagation in the current layer

    Returns:
    dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
    dW -- Gradient of the cost with respect to W (current layer l), same shape as W
    db -- Gradient of the cost with respect to b (current layer l), same shape as b
    """
    A_prev, W, b = cache
    m = A_prev.shape[1]
    
    dW = 1.0/float(m) * np.dot(dZ, A_prev.T)
    db = 1.0/float(m) * np.sum(dZ, axis = 1, keepdims = True)
    dA_prev = np.dot(W.T, dZ)
    
    assert(dA_prev.shape == A_prev.shape)
    assert(dW.shape == W.shape)
    assert(db.shape == b.shape)
    
    return dA_prev, dW, db


# #### 5.2 Linear Activation Backward
# 
# Next, we will create a function that merges the two helper functions: **`linear_backward`** and the backward step for the activation **`linear_activation_backward`**. 
# 
# 
# ```python
# dZ = sigmoid_backward(dA, activation_cache)
# ```
# 
# ```python
# dZ = relu_backward(dA, activation_cache)
# ```
# 
# If $g(.)$ is the activation function, 
# `sigmoid_backward` and `relu_backward` compute $$dZ^{[l]} = dA^{[l]} * g'(Z^{[l]}) $$. 

# In[8]:


def linear_activation_backward(dA, cache, activation):
    """
    Implement the backward propagation for the LINEAR->ACTIVATION layer.
    
    Arguments:
    dA -- post-activation gradient for current layer l 
    cache -- tuple of values (linear_cache, activation_cache) we store for computing backward propagation efficiently
    activation -- the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"
    
    Returns:
    dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
    dW -- Gradient of the cost with respect to W (current layer l), same shape as W
    db -- Gradient of the cost with respect to b (current layer l), same shape as b
    """
    linear_cache, activation_cache = cache
    if (activation == 'sigmoid'):
        dZ = sigmoid_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)
        
    elif (activation == 'relu'):
        dZ = relu_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)
        
    return dA_prev, dW, db


# #### 5.3 L model backward
# 
# Now we will implement the backward function for the whole network. Recall that when we implemented the `L_model_forward` function, at each iteration, we stored a cache which contains (X,W,b, and z). In the back propagation module, we will use those variables to compute the gradients. Therefore, in the `L_model_backward` function, we will iterate through all the hidden layers backward, starting from layer $L$. On each step, we will use the cached values for layer $l$ to backpropagate through layer $l$. Figure 5 below shows the backward pass. 
# 
# 
# ** Initializing backpropagation**:
# To backpropagate through this network, we know that the output is, 
# $A^{[L]} = \sigma(Z^{[L]})$. The code thus needs to compute `dAL` $= \frac{\partial \mathcal{L}}{\partial A^{[L]}}$.
# To do so, use this formula:
# ```python
# dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL)) # derivative of cost with respect to AL
# ```
# 
# We can then use this post-activation gradient `dAL` to keep going backward. We can now feed in `dAL` into the LINEAR->SIGMOID backward function we implemented (which will use the cached values stored by the L_model_forward function). After that, we will have to use a `for` loop to iterate through all the other layers using the LINEAR->RELU backward function. We should store each dA, dW, and db in the grads dictionary. To do so, use this formula : 
# 
# $$grads["dW" + str(l)] = dW^{[l]}\tag{15} $$
# 
# For example, for $l=3$ this would store $dW^{[l]}$ in `grads["dW3"]`.

# In[9]:


def L_model_backward(AL, Y, caches):
    """
    Implement the backward propagation for the [LINEAR->RELU] * (L-1) -> LINEAR -> SIGMOID group
    
    Arguments:
    AL -- probability vector, output of the forward propagation (L_model_forward())
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat)
    caches -- list of caches containing:
                every cache of linear_activation_forward() with "relu" (it's caches[l], for l in range(L-1) i.e l = 0...L-2)
                the cache of linear_activation_forward() with "sigmoid" (it's caches[L-1])
    
    Returns:
    grads -- A dictionary with the gradients
             grads["dA" + str(l)] = ... 
             grads["dW" + str(l)] = ...
             grads["db" + str(l)] = ... 
    """
    grads = {}
    L = len(caches) # the number of layers
    m = AL.shape[1]
    Y = Y.values.reshape(AL.shape) # after this line, Y is the same shape as AL
    
    # Initializing the backpropagation
    dAL = -(np.divide(Y, AL) - np.divide((1.0 - Y),(1.0 - AL)))
    
    # Lth layer (SIGMOID -> LINEAR) gradients. Inputs: "dAL, current_cache". Outputs: "grads["dAL-1"], grads["dWL"], grads["dbL"]
    current_cache = caches[L - 1]
    grads['dA' + str(L - 1)], grads['dW' + str(L)], grads['db' + str(L)] = linear_activation_backward(dAL, current_cache, activation = 'sigmoid')
    
    # Loop from l=L-2 to l=0
    for l in reversed(range(L-1)):
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads['dA' + str(l+1)], current_cache, activation = 'relu')
        grads['dA' + str(l)] = dA_prev_temp
        grads['dW' + str(l+1)] = dW_temp
        grads['db' + str(l+1)] = db_temp
        
    return grads


# #### 5.4 Updating the Parameters
# 
# In this section we will update the parameters of the model, using gradient descent: 
# 
# $$ W^{[l]} = W^{[l]} - \alpha \text{ } dW^{[l]}  $$ 
# $$ b^{[l]} = b^{[l]} - \alpha \text{ } db^{[l]} $$
# 
# where $\alpha$ is the learning rate. After computing the updated parameters, store them in the parameters dictionary. 

# In[10]:


def update_parameters(parameters, grads, learning_rate):
    """
    Update parameters using gradient descent
    
    Arguments:
    parameters -- python dictionary containing your parameters 
    grads -- python dictionary containing your gradients, output of L_model_backward
    
    Returns:
    parameters -- python dictionary containing your updated parameters 
                  parameters["W" + str(l)] = ... 
                  parameters["b" + str(l)] = ...
    """
    L = len(parameters) // 2 #number of layers in the neural network
    # Update rule for each parameter. Use a for loop.
    for l in range(L):
        parameters['W' + str(l+1)] = parameters['W' + str(l+1)] - (learning_rate * grads['dW' + str(l+1)])
        parameters['b' + str(l+1)] = parameters['b' + str(l+1)] - (learning_rate * grads ['db' + str(l+1)])
        
    return parameters


# ### 6 - Architecture of the model
# 
# Let's build a L-layer deep neural network
# 
# #### General methodology
# 
# As usual we will follow the Deep Learning methodology to build the model:
#     1. Initialize parameters / Define hyperparameters
#     2. Loop for num_iterations:
#         a. Forward propagation
#         b. Compute cost function
#         c. Backward propagation
#         d. Update parameters (using parameters, and grads from backprop) 
#     4. Use trained parameters to predict labels
# 
# Let's now implement those two models!

# ### 7. Deep Neural Network

# In[11]:


def L_layer_model(X, Y, layer_dims, learning_rate = 0.0075, num_iterations = 3000, print_cost = False):
    """
    Implements a L-layer neural network: [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID.
    
    Arguments:
    X -- data, numpy array of shape (number of examples, num_px * num_px * 3)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples)
    layers_dims -- list containing the input size and each layer size, of length (number of layers + 1).
    learning_rate -- learning rate of the gradient descent update rule
    num_iterations -- number of iterations of the optimization loop
    print_cost -- if True, it prints the cost every 100 steps
    
    Returns:
    parameters -- parameters learnt by the model. They can then be used to predict.
    """
    np.random.seed(1)
    costs = []   #to keep track of the cost
    
    # Initialize parameters dictionary
    parameters = initialize_parameters(layer_dims)
    
    # Loop (Gradient Descent)
    for i in range(0, num_iterations):
        
        # Forward propagation: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.
        AL, caches = L_model_forward(X, parameters)
        
        # Compute cost.
        cost = compute_cost(AL, Y)
        
        # Backward propagation.
        grads = L_model_backward(AL, Y, caches)
        
        # Update Parameters
        parameters = update_parameters(parameters, grads, learning_rate)
        
        # Print the cost every 100 training example
        if print_cost and i%100 == 0:
            print('Cost after iteration %i: %f' %(i, cost))
        if print_cost and i%100 == 0:
            costs.append(cost)
            
    # Plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title('Learning rate =' + str(learning_rate))
    plt.show()
    
    return parameters


# ### 8. Prediction

# In[12]:


def predict(X, y, parameters):
    """
    This function is used to predict the results of a  L-layer neural network.
    
    Arguments:
    X -- data set of examples you would like to label
    parameters -- parameters of the trained model
    
    Returns:
    p -- predictions for the given dataset X
    """
    m = X.shape[1]
    n = len(parameters) // 2    #number of layers in the network
    p = np.zeros((1, m))
    
    # Forward propagation
    probas, caches = L_model_forward(X, parameters)
    
    # convert probas to 0/1 predictions
    for i in range(0, probas.shape[1]):
        if (probas[0, i] > 0.5):
            p[0, i] = 1
        else:
            p[0, i] = 0
            
    #print results
    #print ("predictions: " + str(p))
    #print ("true labels: " + str(y))
    acc = np.sum(p == y, axis = 1)[0]/float(m)
    print("Accuracy: "  + str(acc))

    
    return p

