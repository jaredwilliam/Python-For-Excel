# Chapter 4. NumPy Foundations
NumPy is the core package for scientific computing in Python and is the backbone of pandas. 
## Getting Started with NumPy

### NumPy Array
To perform array-based calculations with nested lists you would have to write some sort of loop. For example...

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print([[i+1 for i in row] for row in matrix])

Out: [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
```

This isn't very readable and can become slow with with very large arrays. Using NumPy arrays instead of Python lists can make your calculations a couple to hundred times faster. 

Let's create a one- and two-dimensional array to work with throughout this chapter:

```python
# First, import NumPy
import numpy as np

# Constructing an array with a simple list results in a 1d array
array1 = np.array([10, 100, 1000.])

# Constructing an array with a nested list results in a 2d array
array2 = np.array([[1., 2., 3.,],
                   [4., 5., 6.]])
```

### Vectorization and Broadcasting


### Universal Functions (ufunc)

## Creating and Manipulating Arrays

### Getting and Setting Array Elements

### Useful Array Constructors

### View vs. Copy

## Conclusion
