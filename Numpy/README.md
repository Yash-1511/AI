# Numpy Tutorial

- Numpy is short for ```Numerical python```
- Numpy is used for working with Arrays.

# Installation Numpy

```bash
pip install numpy
```

# Importing Numpy

```bash
import numpy as np
```

## Example

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```
# Anatomy of Numpy Array
![numpy array](nparray.png)

# Creating Arrays

NumPy is used to work with arrays. The array object in NumPy is called ndarray.

```python
# array function to create ndarray
# single dimension array
arr = np.array([1,2,3,4,5])
type(arr)
# numpy.ndarray
```

## Multidimensional Arrays

```python
mdarr = np.array([[1,2,3],[4,5,6]])
mdarr

# output looks like
''' array([[1, 2, 3],
       [4, 5, 6]]) '''
```

<br>

>**Note:**<br>
> Numpy Array indexes starts at 0.

```python
arr[1]
# prints 2
mdarr[0][2]
# prints 3
```

## How to check array dimensions?

```python
arr.ndim
# prints 1
```

## How to check array shape?
```python
arr = np.array([1,2,3,4])
arr.shape
# prints (4,)
```
## Another method to create arrays

Besides creating an array from a sequence of elements, you can easily create an array filled with 0’s. 
```python
np.zeros(2)
# array([0., 0.])
```
or an array filled with 1's:
```python 
np.ones(2)
# array([1., 1.])
```

### Empty method
The function empty creates an array whose initial content is random and depends on the state of the memory.
```python
np.empty(2)
# array([ 3.14, 42.  ])
```

### arange method
You can create an array with a range of elements

Similar like python range function
```python
np.arange(4)
# array([0,1,2,3])
np.arange(1,5)
# array([1,2,3,4])
```

# numpy is a famous library for numerical operations on datasets.