class Parent:
    def say_hello(self):
        print('hello')


class Child(Parent):
    def say_hello(self):
        print('yo')


obj = Child()
obj2 = Parent()
obj.say_hello()
obj2.say_hello()