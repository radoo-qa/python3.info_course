"""
Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isclass(Admin)
    >>> assert isclass(MyAccount)
    >>> assert issubclass(MyAccount, Account)
    >>> assert issubclass(MyAccount, User)
    >>> assert issubclass(MyAccount, Admin)

    >>> assert issubclass(Account, object)
    >>> assert issubclass(User, Account)
    >>> assert issubclass(Admin, User)
    >>> assert issubclass(MyAccount, Admin)

    >>> assert len(Account.__subclasses__()) == 1
    >>> assert len(User.__subclasses__()) == 1
    >>> assert len(Admin.__subclasses__()) == 1
    >>> assert len(MyAccount.__subclasses__()) == 0

English:
    1. Create class `MyAccount` from classes `Account`, `User`, `Admin`
    2. Use multilevel inheritance
    3. Assignment demonstrates syntax, so do not add any attributes and methods
    4. Run doctests - all must succeed

"""


class Account:
    pass

class User(Account):
    pass

class Admin(User):
    pass

class MyAccount(Admin):
    pass