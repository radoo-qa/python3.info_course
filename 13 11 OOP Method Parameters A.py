"""
* Assignment: OOP Method Syntax

English:
    1. Define class `Calculator`
    2. Define method `add` in class `Calculator`
    3. Method `add` take `a` and `b` as arguments
    4. Method returns sum of `a` and `b`
    5. Run doctests - all must succeed


Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Calculator)
    >>> calc = Calculator()
    >>> assert ismethod(calc.add)
    >>> calc.add(1, 2)
    3
"""

class Calculator:
    def add(self, a, b):
        return a + b