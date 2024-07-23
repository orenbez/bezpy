import requests

class MyClass:
    class_attribute = 5

    def __init__(self):
        self.value = 2

    def do_something(self):
        return "hello {}".format(self.value)


class MyClass3:

    def __init__(self):
        self.value = 2

    @staticmethod
    def method():
        return 3

def get_value():
    return MyClass.class_attribute

def my_function():
    return 7

def divide_me(x, y):
    return x / y

def another_func():
    return my_function()

def my_class():
    x = MyClass()
    return (x.value, x.class_attribute)

# ======================================================================================================================
class MyClass2:
    def __init__(self, data):
        print("Real object initialized")
        self.data = data

    def get_data(self):
        print("Real object get_data")
        return self.data


def foo(obj: MyClass2):
    print("Object instance:", obj)
    return obj.get_data()

# ======================================================================================================================
class Blog:
    def __init__(self, name):
        print("Real object initialized")
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)