"""
* Assignment: OOP Init Define

English:
    1. Create one class `Hello`
    2. At initialization instance print `hello world`
    3. Do not store any values
    4. Run doctests - all must succeed


Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = Hello()
    hello world
    >>> vars(result)
    {}
"""

class Hello:
    def __init__(self):
        print('hello world')


