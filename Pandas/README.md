# Pandas Tutorial

- Pandas is a Python library.

- Pandas is used to analyze data.

- It has functions for analyzing, cleaning, exploring, and manipulating data.

- Pandas can clean messy data sets, and make them readable and relevant.

- Relevant data is very important in data science.

# Installation

```bash
pip install pandas
```

# Importing pandas

```python
import pandas as pd
```

# Pandas Series

- A Pandas Series is like a column in a table.
- one Dimensional Array

```python
name = ["yash","parth","jatin"]
name_series = pd.Series(data)
name_series
```

# Pandas DataFrame

- A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array.

```python
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

```python
df = pd.read_csv("weather.csv")
df
```

# Export CSV

```python
df.to_csv("filename.csv")
```
# Read JSON

- Big data sets are often stored, or extracted as JSON.

```python
df = pd.read_json("data.json")
df
```

# Viewing the Data

### head() method

```python
df = pd.read_csv("weather.csv")
df.head(3)
```

>**Note:**<br>
> If the number of rows is not specified,the head() method will return the top 5 rows.

<br>

### tail() method

```python
df = pd.read_csv("weather.csv")
df.tail(3)
```

>**Note:**<br>
> If the number of rows is not specified,the tail() method will return the top 5 rows.

<br>

### describe() method

describe() shows a quick statistic summary of your data:

```python
df.describe()
```

### info() method

The DataFrames object has a method called info(), that gives you more information about the data set.

```python
df.info()
```

### display index and columns

```python
# displaying indexes
df.index
# displaying columns
df.columns
# diplaying columns datatypes
df.dtypes
```

# Selecting Data

## Getting
Selecting a single column, which yields a Series, equivalent to df.day:

```python
df['day']
```

## Selection By Label
loc selects rows and columns with specific labels

```python
df.loc[2]
```

## Selection By Position
iloc selects rows and columns at specific integer positions

```python
df.iloc[3]
```

# Missing Data
pandas primarily uses the value np.nan to represent missing data. 

# Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad Data could be:
- Empty cells
- Data in wrong Format
- wrong data
- duplicate data

# Missing Data set
|  | Make     | color  | Odometer | price |
| :---| :-------- | ----------| --------- | ------|
| `0` | `Toyota` | `White` | `150043.0` | `$4000`
| `1` | `Honda` | `Red` | `150043.0` | `$5000`
| `2` | `Toyota` | `Blue` | NaN | `$7000`
| `3` | `BMW` | `Black` | `150043.0` | `$22000`
| `4` | `Nissan` | `White` | `150043.0` | `$4000`
| `5` | `Toyota` | `Black` | NaN | `$4600`
| `6` | `Honda` | `Red` | NaN | `$7500`

## Remove Rows

One way to deal with empty cells is to remove rows that contain empty cells.
```python
df = pd.read_csv('missing_data.csv')

new_df = df.dropna()
new_df

# rows have been removed (row 2,5 and 6).
```
>**Note:**<br>
> By default, the dropna() method returns a new DataFrame, and will not change the original.

If you want to change the original DataFrame, use the inplace = True argument:

```python
df.dropna(inplace=True)
```
<hr>

## Replace Empty Values
The fillna() method allows us to replace empty cells with a value.

```python
df.fillna(130, inplace = True)
```

## Replace Only For Specified Columns

```python
df["Odometer"].fillna(130,inplace=True)
```

## Rename Columns

```py
df.rename(columns={"Odometer":"Odometer (km)"},inplace=True)
```

# Apply
Applying functions to the data

```py
df["odometer"].apply(lambda x: x / 1.6)
```


## Authors

- [@yashparmar](https://www.github.com/Yash-1511)