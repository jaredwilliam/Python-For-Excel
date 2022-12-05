import numpy as np

# Constructing an array with a simple list results in a 1d array
array1 = np.array([10, 100, 1000.])

# Constructing an array with a nested list results in a 2d array
array2 = np.array([[1., 2., 3.],
                   [4., 5., 6.]])

'''
    If you build the sum of a scaler and a NumPy array, NumPy will perform 
    an element-wise operation, which means you don't have to loop through
    elements yourself. This is called vectorization. 
'''
# print(array2 + 1)

'''
    The same principle applies when you work with two arrays: NumPy
    performs the operation element-wise. 
'''
print(array2 * array2)