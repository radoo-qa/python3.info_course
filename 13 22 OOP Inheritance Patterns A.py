"""
* Assignment: OOP InheritancePatterns Simple

English:
    1. Create class `Account`
    2. Create class `User` which inherits from `Account`
    3. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert issubclass(User, Account)
"""

class Account:
    pass

class User(Account):
    pass