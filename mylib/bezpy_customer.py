import random

class Customer:
    """This is Bank Customer Class"""    # Optional class documentation string
    bank_name = "Barclays"               # static class variable  (its lifetime is the entire run of the program)
    bank_code = 579804	                 # static class variable
    customer_count = 0                        # static class variable - total open accounts
    __private_value = "Secret"           # PRIVATE static class variable, dunder. can only be accessed by a function below or subclass; can be modified
    _protected_value = "protect me"      # Single underscore does not PROTECT, same as public but indicates shouldn't be accessing/modifying directly

    # THE INITIALIZER will set up class ATTRIBUTES
    def __init__(self, name, status, bal=0.0, salary=0.0, profession=None):  # THE CONSTRUCTOR, balance is defaulted
        self.name = name               # By default all class variables are PUBLIC
        self.account_number = int(random.random() * 1000000)
        self.status = status           # e.g. 'Gold', 'Silver', 'Bronze'
        self.balance = bal             # Note the variable name 'bal' is not the same as the instance name 'balance'
        self.__salary = salary         # PRIVATE attribute (dunder) can only be accessed by a function below or subclass; can be modified
        self._profession = profession  # PROTECTED attribute (one undescore) same as Public but '_' serves as a warning to protect the field
        Customer.customer_count += 1        # Increments the static variable
        self.weight = 79

    # Note: can use any word for 1st parameter instead of self,  but word 'self' is the convention to mean that you must call this function with an instance.
    def withdraw(self, amount):  # self is the first variable which is the object calling 'withdraw'  x.withdraw(10) is treated like Customer.withdraw(x,10)
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')  # if this is executed it will stop the control at runtime and exit the program
        self.balance -= amount
        print(f'a withdrawal of ${amount} has been made')
        return self.balance

    def set_balance(self, balance=0.0, status=None):  # OVERLOADING in Python doesn't require you to re-write the function
        self.balance = balance
        if status:
            self.status = status  # CHANGE STATUS

    def deposit(self, amount):
        self.balance += amount
        print(f'a deposit of ${amount} has been made. Total:{self.balance}')
        return self.balance

    def display_customer(self):
        print(Customer.bank_name, Customer.bank_code, Customer.customer_count, self.name, '$' + str(self.balance),
              self.status, Customer.__private_value, '$' + str(self.__salary), self._profession, sep='|')
        # Customer.__private_value can't be accessed using an external call from main and would give error

    @staticmethod
    def display_total():
        # since we don't have 'self' parameter, we can only call with class by either Customer.display_total() or instance.display_total()
        """displays total number of accounts for the bank"""
        print(f'Total Accounts: {Customer.customer_count}')

    @classmethod
    def class_foo(cls):
        """Can call by class or instance but will implicitly be called by class either way"""
        print(f"{cls.__name__} executed class_foo()")

    def display_salary(self):
        """displays customers salary"""
        print("Customer Salary:", self.__salary)

    # Class DESTRUCTOR
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

    def _protected_function(self):
        print('Same idea as a protected attribute, intended for internal use but can be called externally')

    @staticmethod
    def __private_function():
        print('Same idea as a private attribute, accessed internally only, or will give error')

    @staticmethod
    def check_range(x):
        """helper function"""
        if 0 < x < 1000000:
            return True
        else:
            return False


if __name__ == '__main__':
    x = Customer('Jeff Knupp', "Bronze", 1000.0, 85000)    # x is now referred to as an 'object' or 'instance' of Class Customer
    y = Customer('Fred Blogs', "Gold", 10000.0)
    z = Customer('Jason Freedman', "Bronze")
    x2 = Customer('Dave Peters', 'Gold', 10000.0, 85000, 'Gardener')

    x2.display_salary()  # displays private value,  x.__salary would fail
    x2._profession  # acesses profession but the single underscore serves as a convention warning that you are doing something naughty

    w = z  # this variable will point to the same object as z
    w.name = 'Amanda Henry'  # changes name of 'z'
    getattr(w, 'name')  # same as w.name

    x.deposit(30)
    x.withdraw(20)  # same as Customer.withdraw(x, 20)
    # Customer.withdraw(20) would give an error
    # withdraw(x,20) this would give an error

    x.display_customer()
    x.set_balance()
    x.set_balance(500)
    x.set_balance(5000, 'Gold')  # example of OVERLOADING in python

    y.display_customer()
    Customer.bank_name = "HSBC"  # static class variable modified
    z.display_customer()
    Customer.display_total()
    x2.display_total()   # same as above
    z.display_customer()
    # print (Customer.__hidden_value) this would give an error

    delattr(z, 'status')  # to delete an attribute. equivalent to "del z.status"
    print(hasattr(z, 'status'))  # to check if an attribute exists or not.
    setattr(z, 'status', 'Bronze')  # to set an attribute. If attribute does not exist, then it would be created.
    print(getattr(x, 'status'))  # to access the attribute of object.

    print(Customer.__dict__)    # Dictionary containing the class's namespace. Same as vars(Customer)
    print(Customer.__doc__)     # Class documentation string or none, if undefined.  'This is Bank Customer Class'
    print(Customer.__name__)    # Class name ie. 'Customer'.
    print(Customer.__module__)  # Module name in which the class is defined i.e. 'Customer' since file is Customre.py This attribute is "__main__" in >> interactive mode. or if run in this file
    print(Customer.__bases__)   # Displays the base classes, in the order of their occurrence in the base class list. Minimally will display (object,) which is the parent class of all classes

    Customer.bank_code = 579805  # reassigns for entire class
    x.bank_code = 579806         # assigns an instance attribute which shares the same name as the class static variable
    x.bank_code             # returns 579806
    x.__class__.bank_code   # returns the class variable value 579805
    x.__dict__              # returns all of x's values

    # Destroying Objects (Garbage Collection)
    print(id(x), id(y), id(z), id(w))  # prints the ids of the objects = RAM memory location
    del x                              # deletes the identifier.  Object will still be there if another identifier is assigned to it
    del y
    del z
    print(id(w))  # this is still undeleted but will be deleted automatically when code exits

    # private values can be reffered to as Class 'Encapsulation'.  The general idea is to hide attributes/functionality from the user with a simple API front for them to use
