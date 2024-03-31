# Jafar
A python module that will reduce the Standard Deviation of a dataset to approach `lim x -> +inf : f(x)`

# Définition
```py
def result(d:dict[int, int], t:int, size:int, p:list[int], tirage:int=1) -> list[Any, float]:
```

# Usage

To use it , import the module Jafar and it function *lecture_csv* and *result*.

```py
from jafar import predire;

# List of number you want it to find (optional)
prediction:list[int] = [3]
colonnes:list[str]   = ["numero_chance"]
csvFile:str          = "loto_201911.csv"

# Parsing the DataFrame and calculate the lower Standard Deviation
predire(csv=csvFile, col=colonnes, prediction=prediction)

>>> [(X, 0.xxx), (Y, 0.yyy), (Z, 0.zzz), ...]
```

# DocString

```py
predire(csv:str, col:list[str], *, prediction:list[int]) -> int
```

* `csv` - Path to the csv file were the data are
* `col` - List of column you want to use in the deviation
* `prediction` **optional** - Is the list of the value you expect to appear, the console will overline them in green
