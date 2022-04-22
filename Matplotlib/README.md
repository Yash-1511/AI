# Matplotlib Tutorial

Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

# Installation

```bash
pip install matplotlib
```

# Import

## pyplot

Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias

```python
import matplotlib.pyplot as plt
```

# Example

```python
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]

plt.plot(x, y)
plt.show()
```

# Plotting

- The plot() function is used to draw points (markers) in a diagram.
- By default, the plot() function draws a line from point to point.

```python
import matplotlib.pyplot as plt
%matplotlib inline

x = [1,2,3,4,5,6,7]
y = [50,24,56,56,75,43,23]

plt.plot(x,y)
```

## plotting without line

```python
plt.plot(x,y,'o')
plt.show()
```

# formatting

```python
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')

plt.plot(x,y,color='red',marker='+',linestyle='')
```

- You can use the keyword argument marker to emphasize each point with a specified marker

- You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line.

<a href="https://www.w3schools.com/python/matplotlib_markers.asp" target="_blank"> Markers Reference </a>

<a href="https://www.w3schools.com/python/matplotlib_line.asp" target="_blank"> LineStyle Reference </a>

# Labels

With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

```python
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('Demo Chart')
```

you can use the title() function to set a title for the plot.

# Legend

- A legend is an area describing the elements of the graph. In the matplotlib library, there’s a function called legend() which is used to Place a legend on the axes.

## Example

```python
import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]

plt.plot(days,max_t,label='max')
plt.plot(days,min_t,label='min')
plt.plot(days,avg_t,label='avg')
plt.legend(loc='best')
```

# Grid

you can use grid() function to add grid lines to the plot.

```python
plt.grid()
```

# Bar Chart

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
```

# Horizontal bar

```python
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.hbar(x,y)
plt.show()
```

# Histograms

A histogram is a graph showing frequency distributions.

```python
blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]

plt.hist(blood_sugar, rwidth=0.8) # by default number of bins is set to 10
```

