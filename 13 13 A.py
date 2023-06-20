"""
English:
    1. Create class `Iris` with `features: list[float]` and `label: str` fields
    2. For each row in `DATA` create `Iris` instance with row values
    3. Set class attributes at the initialization from positional arguments
    4. Create method which sums values of all `features`
    5. In `result` gather species and sum of each row
    6. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'setosa': 9.4,
     'versicolor': 16.299999999999997,
     'virginica': 19.3}
"""

DATA = [
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
]


result = {}

class Iris:
    features: list[float]
    label: str

    def __init__(self, features, label):
        self.label = label
        self.features = features

    def sum(self):
        return sum(self.features)


for *feature, label in DATA:
    iris = Iris(feature, label)
    result[iris.label] = iris.sum()

print(result)
