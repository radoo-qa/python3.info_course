"""
* Assignment: OOP Method Nested

English:
    1. Define class `Iris`
    2. `Iris` has:
        a. "sepal_length" type `float`
        b. "sepal_width" type `float`
        c. "petal_length" type `float`
        d. "petal_width" type `float`
        e. "species" type `str`
    3. `Iris` can:
        a. Return number of `float` type attributes
        b. Return list of all `float` type attributes
        c. Return sum of values of all `float` type attributes
        d. Return mean of all `float` type attributes
    4. Use `vars(self)` iteration to return values of numeric fields
    5. Create `setosa` object with attributes set at the initialization
    6. Create `virginica` object with attributes set at the initialization
    7. Method `.show()` returns sum, mean and species name, example:
       a. 'total=10.20 mean=2.55 setosa'
       b. 'total=15.50 mean=3.88 virginica'
    8. Do not use `@dataclass`
    9. Run doctests - all must succeed


Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

    >>> setosa.show()
    'total=10.20 mean=2.55 setosa'
    >>> virginica.show()
    'total=15.50 mean=3.88 virginica'
"""

class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def features(self):
        return [x for x in vars(self).values() if type(x) is float]

    def count_float(self):
        return len(self.features())

    def sum_float(self):
        return sum(self.features())

    def mean_float(self):
        return self.sum_float()/self.count_float()

    def show(self):
        return f"total={self.sum_float()} mean={self.mean_float()} {self.species}"

setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')
print(setosa.show())
print(virginica.show())
