"""
* Assignment: OOP Method Mean
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define class `Stats`
    2. Define method `mean()` in `Stats` class
    3. Method takes `data: list[float]` as an argument
    4. Method returns arithmetic mean of the `data`
    5. Returned value must be rounded to one decimal places
    6. Run doctests - all must succeed



Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Stats)
    >>> stats = Stats()
    >>> assert ismethod(stats.mean)

    >>> stats.mean([1, 2])
    1.5
    >>> stats.mean([5.8, 2.7, 5.1, 1.9])
    3.9
"""

class Stats:
    data: list[float]

    def mean(self, data):
        return round(sum(data) / len(data), 1)