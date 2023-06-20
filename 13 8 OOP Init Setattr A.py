"""
* Assignment: OOP Init Define

English:
    1. Modify code below
    2. Implement method `__init__()` to set attributes:
       `self.name`, `self.country`, `self.date`
    3. Attributes must be set from arguments passed at initialization
    4. Run doctests - all must succeed


Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import ismethod, signature

    >>> mark = Astronaut('Mark', 'USA', '1969-07-21')
    >>> nasa = Astronaut('Nasa', 'USA', '1969-07-21')

    >>> assert ismethod(mark.__init__)
    >>> assert ismethod(nasa.__init__)

    >>> signature(Astronaut.__init__)
    <Signature (self, name, country, date)>
    >>> signature(SpaceAgency.__init__)
    <Signature (self, name, country, date)>

    >>> signature(mark.__init__)
    <Signature (name, country, date)>
    >>> signature(nasa.__init__)
    <Signature (name, country, date)>
"""


# Implement method to set: self.name, self.country, self.date
# Attributes must be set from arguments passed to __init__()
# type: type[Astronaut]
class Astronaut:
    name: str
    country: str
    date: str

    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


# Implement method to set: self.name, self.country, self.date
# Attributes must be set from arguments passed to __init__()
# type: type[Astronaut]
class SpaceAgency:
    name: str
    country: str
    date: str

    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date
