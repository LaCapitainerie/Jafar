# Jafar
A python module that will reduce the Standard Deviation of a dataset to approach `lim x -> +inf : f(x)`

# Définition
```py
def result(d:dict[int, int], t:int, size:int, p:list[int], tirage:int=1) -> list[Any, float]:
```

# Usage

To use it , import the module Jafar and it function *lecture_csv* and *result*.

```py
from Jafar import lecture_csv, result;

# List of number you want it to find (optional)
prediction = [4,12,15,23,42,1]

# Parsing the DataFrame and calculate the lower Standard Deviation
data, times, size = lecture_csv()
result(d=data, t=times, size=size, p=prediction, tirage=1)

>>> [(X, 0.xxx), (Y, 0.yyy), (Z, 0.zzz), ...]
```

# DocString

```py
result(d:dict[int, int], t:int, size:int, p:list[int], tirage:int=1):
```

* `data` - A dict of all the data and their repartition in the DataFrame
* `t` - The number of value in the DataFrame
* `size` - The size of the DataFrame, not the lines but the number of unique values
* `p` **optional** - Is the list of the value you expect to appear, the console will overline them in green
* `tirage` **optional** - Is the number of value you want to draw per tirage
  * default value is 1 as it's the lowest value you can enter
