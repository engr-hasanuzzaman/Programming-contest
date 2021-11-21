# remove punctuations from the strings
```python
import string
s.translate(str.maketrans('', '', string.punctuation))
```

# using `divmod` we can get both quotient and remainder. `divmod(18, 12) -> (1, 6)`