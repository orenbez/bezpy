from email import header
import sys
import unittest
import requests

# ======================================================================================================================
# Tactical fix - quick without testing
# Strategic fix - longer term fix

# Unit Testing ...
# performed by developers to test a specific aspect of a function/method. Compare with 'Functional Testing' below.
# A 'unit test' verifies that one specific aspect of a function’s behavior is correct.
# A 'test case' is a collection of unit tests for a given function.
# A test case with 'full coverage' includes a full range of unit tests covering all the possible ways function is used
# integration test, on the other hand is used to test components that rely on each-other

# Smoke Testing ...
# is a software testing technique performed post software build to verify that the critical
# functionalities of software are working fine. It is executed before any detailed functional or regression
# tests are executed. The main purpose of smoke testing is to reject a software application with defects so that QA
# team does not waste time testing broken software application. In Smoke Testing, the test cases chose to cover the most
# important functionality or component of the system. The objective is not to perform exhaustive testing, but to verify
# that the critical functionalities of the system are working fine.

# Sanity Testing ...
# is a kind of Software Testing performed after receiving a software build, with minor changes in code,
# or functionality, to ascertain that the bugs have been fixed and no further issues are introduced due to these
# changes. The goal is to determine that the proposed functionality works roughly as expected. If sanity test fails,
# the build is rejected to save the time and costs involved in a more rigorous testing.  The objective is “not” to
# verify thoroughly the new functionality but to determine that the developer has applied some rationality (sanity)
# while producing the software.

# Functional Testing ...
# is the testing of the system to validate that the software system will work efficiently as per the functional requirements.
# The main aim of functional testing is to verify that each function works properly against the functional requirements and specifications.
# Done by the testing team, tests are from the perspective of the users.

# ======================================================================================================================
# this program will test these functions below, normally you would just import them
# ======================================================================================================================
def multiply(a,b):
    return a*b

def exit_function():
    sys.exit(5)

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last

    return full_name.title()

class NumClass():
    def __init__(self, num):
        self.num = num
    def add(self, num2):
        return self.num + num2
    def sub(self, num2):
        return self.num - num2

# ======================================================================================================================
# Test Cases:  each method must start def test_...
# ======================================================================================================================
class ExitFunctionTestCase(unittest.TestCase):
    def test_exit_function(self):
       # self.assertRaises(ExpectedException, afunction)
       # self.assertRaises(ExpectedException, afunction, arg1, arg2)
       # self.assertRaises(ExpectedException, Class, self, arg1, arg2)
        with self.assertRaises(SystemExit) as cm:
            exit_function()
            self.assertEqual(cm.exception.code, 5)

class NamesFunctionTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

class MultiplyFunctionTestCase(unittest.TestCase):
    
    def test_numbers_3_4(self):
        self.assertEqual(multiply(3,4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a',3), 'aaa')


class NumClassTestCase(unittest.TestCase):
    def setUp(self):
        "here I can set values or objects to use in the whole test case"
        self.x = NumClass(4)
        self.any_value = 7

    def test_add(self):
        self.assertEqual(self.x.add(3), self.any_value)

    def test_sub(self):
        self.assertEqual(self.x.sub(3), 1)

    def tearDown(self):
        "hear I can change values after executions of tests"        
        pass


# skip can be used to ignore tests
class TestCase5(unittest.TestCase):

    @unittest.skip("reason 1") # will always skip
    def test_01(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(True, "reason 2") # skip based on a condition being True
    def test_02(self):
        self.assertEqual(1, 1)

    @unittest.skipUnless(False, "reason 3") # skip based on a condition being False
    def test_03(self):
        self.assertEqual(1, 1)


# ======================================================================================================================
# Mock & Patch  
# ======================================================================================================================
# https://realpython.com/python-mock-library/
# Would be many reasons a function or process is inconvenient to run in testing
# like http request or database queries and you will want to 'mock' them in testing

from unittest.mock import patch, Mock

# Actually Runs get_value() Without Mock
class TestCase6(unittest.TestCase):
    def test_mock_1(self):
        from mylib.mymock import get_value
        self.assertEqual(get_value(), 5)

# ======================================================================================================================
# This Mocks get_value without actually running it.
# ======================================================================================================================
@patch('mylib.mymock.get_value', return_value=5)   # Note 'mylib.' is needed in the decorator argument
class TestCase7(unittest.TestCase):
    def test_mock_2(self, mock_get_value):
        self.assertEqual(mock_get_value(), 5)

# ======================================================================================================================
# Here patch is only for the function not the whole class
# ======================================================================================================================
class TestCase8(unittest.TestCase):
    @patch('mylib.mymock.get_value', return_value=5)     # <-- moved @patch here so will only cover below test case
    def test_mock_3(self, mock_get_value):
        self.assertEqual(mock_get_value(), 5)

# ======================================================================================================================
# This uses context manager instead of decorator
# ======================================================================================================================
class TestCase9(unittest.TestCase):
    def test_mock_9_1(self):
        with patch('mylib.mymock.get_value', return_value=6) as mock_get_value:  # mock_get_value is of type 'Magic Mock'
            self.assertEqual(mock_get_value(), 6)

    # Note in the patch, lambda *args, **kwargs overrides any input values and returns 'SUCCESS'
    def test_mock_9_2(self):
        from mylib.mymock import my_function, another_func
        with patch('mylib.mymock.my_function', lambda *args, **kwargs: 'SUCCESS') as mocked_function:
            self.assertEqual(mocked_function(), 'SUCCESS')
            self.assertEqual(my_function(), 7)              # <-------- this is not getting mocked
            self.assertEqual(another_func(), 'SUCCESS')     # <-------- this is using mocked_function()  not my_function()

# ======================================================================================================================
# notice the order of association, last patch is first argument
# these arguments mock_divide_me & mock_my_function are instances of MagicMock,
# which is unittest.mock's default mocking object. You can define the behavior of the patched function
# by setting attributes on the returned MagicMock instance
# ======================================================================================================================
@patch('mylib.mymock.my_function', return_value=8)
@patch('mylib.mymock.divide_me', return_value=2)
class TestCase10a(unittest.TestCase):
    def test_mock_10a(self, mock_divide_me, mock_my_function):
        self.assertEqual(mock_divide_me(), 2)
        self.assertEqual(mock_my_function(), 8)


# ================================================  Class Mocking ======================================================
class TestCase10b(unittest.TestCase):
   def test_mock_10b(self):
    from mylib.mymock import my_class
    self.assertEqual(my_class(), (2, 5))   # <---------- no mocking this time

@patch('mylib.mymock.MyClass')
class TestCase10c(unittest.TestCase):
    def test_mock_10c(self, MockClass):
        y = MockClass()
        y.value = 3
        y.class_attribute = 6
        from mylib.mymock import my_class
        self.assertEqual(my_class(), (3, 6))

class TestCase10d(unittest.TestCase):
    def test_mock_10d(self):
        from mylib.mymock import MyClass2, foo
        x = MyClass2(99)
        self.assertEqual(foo(x), 99)   # <---------- no mocking this time

@patch('mylib.mymock.MyClass2')
class TestCase10e(unittest.TestCase):
    def test_mock_10e(self, MockClass2):
        obj = MockClass2.return_value   # obj is a mocked instance of MyClass2
        obj.get_data.return_value = 3
        from mylib.mymock import foo
        self.assertEqual(foo(obj), 3)


def test_mock_10f( ):
    with patch('mylib.mymock.MyClass2') as MockClass2:
        obj = MockClass2()
        obj.get_data.return_value = 3
        from mylib.mymock import foo
        assert foo(obj) == 3

@patch('mylib.mymock.MyClass2')
def test_mock_10ff(MockClass2):
    obj = MockClass2()
    obj.get_data.return_value = 3
    from mylib.mymock import foo
    assert foo(obj) == 3


def test_mock_10g():

    # The mocking happens in the module where target function or object is USED not where the function or class is DEFINED ...
    # so with patch('mylib.mymock.MyClass3') as MockClass3: is WRONG
    with patch('mylib.mymock2.MyClass3') as MockClass3:
        obj = MockClass3()
        obj.value = 3
        from mylib.mymock2 import my_class3
        assert my_class3() == 3


    with patch('mylib.mymock2.MyClass3.method', return_value=4) as MockClass3:
        from mylib.mymock2 import my_class3, test_2
        assert my_class3() == 2  # <-- this is not being mocked
        assert test_2() == 4    # <---- mocking a single class method

class TestCase10g(unittest.TestCase):
    @patch('mylib.mymock.Blog')
    def test_mock_10g(self, MockBlog):
        import mylib
        blog = MockBlog()    # same as blog = MockBlock.return_value
        blog.posts.return_value = [{'userId': 1, 'body': 'message'}]
        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        assert response[0] == {'userId': 1, 'body': 'message'}
        assert MockBlog is mylib.mymock.Blog  # The mock is equivalent to the original
        assert MockBlog.called  # The mock was called

        blog.posts.assert_called_with()       # We called the posts method with no arguments
        blog.posts.assert_called_once_with()  # We called the posts method once with no arguments

        blog.posts(1, 2, 3)
        print(blog.posts.call_args)   # returns call(1, 2, 3)
        blog.posts.assert_called_with(1, 2, 3)
        blog.posts.call_count  # returns number of times called blog.posts()  = 2
        blog.method_calls      # returns [call.posts(), call.posts(1, 2, 3)]
        blog.reset_mock()      # Reset the mock object
        blog.posts.assert_not_called()  # After resetting, posts has not been called.

# ===========================================================================================
# mock.patch() takes a string which will be resolved to an object when applying the patch
# mock.patch.object() takes a direct reference.
# This means that mock.patch() doesn't require that you import the object before patching, 
# while mock.patch.object() does require that you import before patching.

# e.g.
# @patch.object(SomeClass, 'class_method')
# @patch('SomeClass.static_method')
# def test(mock1, mock2):
#     pass


# ===========================================================================================
def call_api():
    try:
        return requests.post("https://www.api.com")
    except requests.exceptions.ConnectionError:
        print("Connection Error occurred")

def call_api2():
    try:
        response = requests.post("https://www.api.com")
        return response.json()
    except Exception as e:
        print(f'Exception Occurred: {e}')
        return e.args[0]


class TestCase11(unittest.TestCase):
    # METHOD 1 - use a real requests.Response() object
    @patch('requests.post')  
    def test_call_api_1(self, mock_post):
        r = requests.Response()
        r.status_code = 200
        r._content = b'''{"number": 1234, "user_id": 1, "name": "john"}'''
        r.headers = {'Content-Type': 'application/json'}
        mock_post.return_value = r
        self.assertEqual(r, call_api())

    # METHOD 2 - use the Mock() object
    @patch('requests.post')
    def test_call_api_2(self, mock_post):                
        r = Mock(status_code=200, headers={'Content-Type': 'application/json'}, json2={"name": "Robin Hood"})
        r.json.return_value = {"number": 1234, "user_id": 1, "name": "James Bond"}
        mock_post.return_value = r
        response = call_api()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json2["name"], "Robin Hood")
        self.assertEqual(response.json()["name"], "James Bond")

    # Mocking the except clause with 'side_effect'
    @patch("requests.post")
    def test_call_api_3(self, mock_post):
        my_mock_response = Mock(status_code=404)
        my_mock_response.json.side_effect = ValueError("here be dragons")
        mock_post.return_value = my_mock_response
        response = call_api2()
        self.assertEqual(response, "here be dragons")

# ======================================================================================================================
# side_effect - instead of the return value you are forcing divide_me to fail and mocking 'e' instead
# if side_effect is an iterable, e.g. list, then each call to the mock will return the next value from the iterable
# ======================================================================================================================
def some_method():
    from mylib.mymock import divide_me
    try:
        return divide_me(5, 7)
    except Exception as e:
        return e.args[0]  # this captures the exception message only

class TestCase12a(unittest.TestCase):
    @patch('mylib.mymock.divide_me', side_effect=ValueError('This was Bad'))
    def test_mock_12_1(self, mock_obj):
        ret = some_method()
        self.assertEqual(ret, 'This was Bad')


def mock_divide_me(a, b):
    print('executed mock_divide_me')
    return a / b

class TestCase12b(unittest.TestCase):
    @patch('mylib.mymock.divide_me', side_effect=mock_divide_me)   # <--- instead of hard coding a return value execute this function instead
    def test_mock_divide_me(self, divide_me):
        self.assertEqual(divide_me(4, 2), 2)



# ===========================================================================================


if __name__ == '__main__':  # this is not required if you are running from command line with python -m unittest
    unittest.main()  # runs all test cases

    

# ======================================================================================================================
# Expected Output from command line: note a dot for each pass, 's' for each skipped
# ======================================================================================================================
# .......sss...
# ----------------------------------------------------------------------
# Ran 13 tests in 0.014s
#
# OK (skipped=3)



# ======================================================================================================================
# From command line (-m=Module)
# ======================================================================================================================
# python -m unittest bezpy_48_unittest.py               # to run tests in this module
# python -m unittest C:\path\unit_test_module.py        # runs all tests in module
# python -m unittest test_path.test_module.TestClass.test_method  # to be specific
# python -m unittest -h  # for help


# ======================================================================================================================
# Test Functions  use help(unittest.Testcase.assertEquals)
# ======================================================================================================================
# assertEqual(function(a),b)
# assertNotEqual
# assertAlmostEqual(function(a),b)  # Checks 1st 7 decimal places
# assertNotAlmostEqual(function(a),b)  # Checks 1st 7 decimal places
# assertCountEqual
# assertDictEqual
# assertNotEqual(function(a),b)
# assertTrue(x)
# assertFalse(x)
# assertGreater
# assertGreaterEqual
# assertLess
# assertLessEqual
# assertListEqual
# assertLogs
# assertMultiLineEqual
# assertIs(function(a),b)
# assertIsNot(function(a), b)
# assertIsNone(function(a))
# assertIsNotNone(function(a))
# assertIn(function(a), b)
# assertNotIn(function(a), b)
# assertIsInstance(function(a), b)
# assertNotIsInstance(function(a), b)
# assertRegex
# assertNotRegex
# assertRegexpMatches
# assertNotRegexMatches
# assertRaises(ValueError, function, a)  - test to see if 'function' raises a 'ValueError' with input 'a'
# assertRaisesRegex
# assertRaisesRegexp
# assertSequenceEqual
# assertSetEqual


# ======================================================================================================================
# Deprecated
# ======================================================================================================================
# assertEquals
# assertAlmostEquals
# assertNotAlmostEquals
# assertNotEquals

# ======================================================================================================================
# Deprecated in 3.11
# ======================================================================================================================
# unittest.findTestCases()     # Deprecated in 3.11
# unittest.makeSuite()         # Deprecated in 3.11
# unittest.getTestCaseNames()  # Deprecated in 3.11

# Use the corresponding methods in TestLoader module instead:
# unittest.TestLoader.loadTestsFromModule()
# unittest.TestLoader.loadTestsFromTestCase()
# unittest.TestLoader.getTestCaseNames()

# ======================================================================================================================
# SMOKE TESTING
# ======================================================================================================================
# is performed to ascertain that the critical functionalities of the program are working fine.	
# exercises the entire system from end to end.	
# is usually documented and scripted.	
# is performed by the developers or testers.	
# is a well elaborate and planned testing.	
# is a wide and deep testing.	
# is a subset of Acceptance testing.	
#
# ======================================================================================================================
# SANITY TESTING
# ======================================================================================================================
# is done at random to verify that each functionality is working as expected.
# exercises only the particular component of the entire system.
# is not documented and is unscripted.
# is usually performed by testers.
# is not a planned test and is done only when there is a shortage of time.
# is a wide and shallow testing.
# is a subset of Regression Testing.


# ======================================================================================================================
# Stress & Load Testing
# ======================================================================================================================
# tests limits of infrastructure = operation envelope

# ======================================================================================================================
# Performance testing 
# ======================================================================================================================
# test speed of runs with large datasets