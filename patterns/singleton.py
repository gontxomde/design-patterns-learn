import traceback


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            # This calls the __init__ method in the Connection class
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Connection(metaclass=Singleton):

    def __init__(self, **kwargs):
        self.age = kwargs.get('age', 0)

    def refresh_connection(self):
        return print("Connection refreshed")

class Person(metaclass=Singleton):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'BOB')


if __name__ == '__main__':

    c1 = Connection(age=2)
    c2 = Connection(age=3)

    if id(c1) == id(c2):
        print("Success")

    else:
        print("Error")

    c1.refresh_connection()
    p1 = Person(name='Gonzalo')
    print(p1.name)