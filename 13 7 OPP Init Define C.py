"""
* Assignment: OOP Init Define

English:
    1. Modify code below
    2. Define `__init__()` method in both classes
    3. Signature should reflect class attributes
    4. Method `__init__()` raises exception `NotImplementedError`
    5. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import ismethod, signature

    >>> mark = Astronaut('Mark', 'USA', '1969-07-21')
    Traceback (most recent call last):
    NotImplementedError

    >>> nasa = Astronaut('Nasa', 'USA', '1969-07-21')
    Traceback (most recent call last):
    NotImplementedError

    >>> signature(Astronaut.__init__)
    <Signature (self, name, country, date)>
    >>> signature(SpaceAgency.__init__)
    <Signature (self, name, country, date)>
"""


class Astronaut:
    def __init__(self, name=None, country=None, date=None):
        name: str
        country: str
        date: str


class SpaceAgency:
    def __init__(self, name=None, country=None, date=None):
        name: str
        country: str
        date: str