# Pandas Tutorial

- Pandas is a Python library.

- Pandas is used to analyze data.

- It has functions for analyzing, cleaning, exploring, and manipulating data.

- Pandas can clean messy data sets, and make them readable and relevant.

- Relevant data is very important in data science.

# Installation

```sh
pip install pandas
```

# Importing pandas

```py
import pandas as pd
```

# Pandas Series

- A Pandas Series is like a column in a table.
- one Dimensional Array

```py
name = ["yash","parth","jatin"]
name_series = pd.Series(data)
name_series
```

# Pandas DataFrame

- A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array.

```py
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
df
```

# Read CSV

- A simple way to store big data sets is to use CSV files (comma separated files).
- importing csvs

```py
df = pd.read_csv("weather.csv")
df
```

# Export CSV

```py
df.to_csv("filename.csv");
```
# Read JSON

- Big data sets are often stored, or extracted as JSON.

```py
df = pd.read_json("data.json")
df
```

# Viewing the Data

### head() method

```py
df = pd.read_csv("weather.csv")
df.head(3)
```

>**Note:**<br>
> If the number of rows is not specified,the head() method will return the top 5 rows.

<br>

### tail() method

```py
df = pd.read_csv("weather.csv")
df.tail(3)
```

>**Note:**<br>
> If the number of rows is not specified,the tail() method will return the top 5 rows.

<br>

## Authors

- [@yashparmar](https://www.github.com/Yash-1511)