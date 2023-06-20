"""
* Assignment: OOP Init Define

English:
    1. Create one class `Echo`
    2. Value `text` must be passed at the initialization
    3. At initialization instance print `text`
    4. Do not store values in the instances (only print on instance creation)
    5. Do not use `@dataclass`
    6. Run doctests - all must succeed


Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> _ = Echo('hello')
    hello
    >>> _ = Echo('world')
    world
    >>> result = Echo('Test')
    Test
    >>> vars(result)
    {}
"""

class Echo:
    def __init__(self, text):
        print(text)
