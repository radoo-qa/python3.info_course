"""
English:
    1. Create class `Astronaut` which inherits from `Person` +
    2. Class `Astronaut` takes two arguments `name` and `mission`
    3. Set attribute `mission` in `Astronaut` inicializer method
    4. Call initializer method of `Person` passing `name` as an argument
    5. Define method `show()` returning name and after coma - a mission name
    6. Run doctests - all must succeed

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> watney = Astronaut('Watney', 'Ares 3')
    >>> watney.show()
    'Watney, Ares 3'
    >>> lewis = Astronaut('Lewis', 'Ares 3')
    >>> lewis.show()
    'Lewis, Ares 3'
"""


class Person:
    def __init__(self, name):
        self.name = name


class Astronaut(Person):
    def __init__(self, name, mission):
        self.mission = mission
        super().__init__(name)

    def show(self):
        return f"{self.name}, {self.mission}"


