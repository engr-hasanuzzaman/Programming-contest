# remove punctuations from the strings
```python
import string
s.translate(str.maketrans('', '', string.punctuation))
```

# using `divmod` we can get both quotient and remainder. `divmod(18, 12) -> (1, 6)`

# `(12).byte_length()` return the byte size of the 12
- `int` max size in python limited by the machine
- to convert string to int or change the base we will use `int(str_num, base)` method
- `divmod(18,12) -> (1, 6)`
- `10.5.as_integer_ratio()` -> `(21, 2)`
