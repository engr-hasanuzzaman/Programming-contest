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

### The `discard()` method removes the specified item from the set. This method is different from the `remove()` method, because the `remove()` method will raise an error if the specified item does not exist, and the `discard()` method will not

- `"sumon".rjust(50, '_')` -> `_____________________________________________sumon`
- `"sumon".ljust(50, '_')` -> `sumon_____________________________________________`

### Using `locals()` we can see list of available local variables