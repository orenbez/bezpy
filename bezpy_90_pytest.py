# READ_ME: https://realpython.com/pytest-python-testing/
# READ_ME: https://levelup.gitconnected.com/a-comprehensive-guide-to-pytest-3676f05df5a0

# Alternative to 'unittest' and 'nosetest'
# Requires 'pip install pytest'
# https://www.guru99.com/pytest-tutorial.html
# https://docs.pytest.org/en/7.1.x/
# run 'py.test -h' in command prompt confirms pytest library is installed, displays help file

# with py.test,  assertions are checked that return either True or False status.
# If an assertion fails in a test method, then that method execution is stopped there.
# The remaining code in that test method is not executed, and Pytest assertions will continue with the next test method.


# Note in the command line you can use 'py.test' and 'pytest' interchangeably to run the tests

# run 'pytest' tosearch recursively & test all files starting with "test_xxx.py
# run 'pytest <path>' tosearch recursively & test all files starting with "test_xxx.py in <path>
# run 'pytest --cov=<path>' i think this is the same as above
# run 'pytest bezpy_90_pytest.py'  to only run tests in this file
# run 'pytest <filename1> <filename2>' to only run tests in the listed files

# run 'pytest bezpy_90_pytest.py -k method -v -s'
#       -k 'method' - will select all test functions with substring 'method' in the function name e.g. test_method_5()
#       -v will give verbose results
#       -vv will give even  more verbose results
#       -q will give quiet results (oppostite of verbose)
#       -s will allow print() to print to stdout
#       -rP will allow print() to stdout for tests which pass  (but not for teardown functions)
#       -rF will allow print() to stdout for tests which fail  (but not for teardown functions)

# run 'pytest -log-cli-level=DEBUG test.py'  for logging to stdout 

# run 'pytest -m <name>'
#     -m <name> mentions the marker name and will identify any tests with decorator @pytest.mark.<name>
#     this option requires a pytest.ini file

# run pytest file_name.py::function_name  to test a single function

# run pytest -v .\bezpy_90_pytest.py --junit-xml='result.py'
# to generate results in XML format which we can fed to Continuous Integration servers for further processing

# run pytest --no-cov  # this will disable coverage data which would check %ge of code covered with your pytests
# run pytest --cov-fail-under=80  # sets fail if your tests cover less than 80% of the code

# use ...  assert <CONDITION>, "AssertionError message if fails"

# install pytest-xdist to run tests over multiple cores in parallel

# ======================================================================================================================
# To Debug pytest in pycharm, stopping at breakpoints ...
# ======================================================================================================================
# https://stackoverflow.com/questions/40718760/unable-to-debug-in-pycharm-with-pytest
# 1. right-click on green arrow for the test
# 2. select 'Modify run configuration...'
# 3. Set 'Additional Arguments' to --no-cov and click Ok
# 4. right-click on green arrow for the test and select 'Debug'
# if pytests are missing the green triangle in pycharm 
# File -> Settings -> Tools -> Python Integrated Tools -> Testing -> Default test runner = pytest
# Note that the green triangle and debugging option is only available for functions 
# called  'test_xxx'  or   from the if __name__ == '__main__' line.

import pytest  # needed only for decorators
from platform import system
# ======================================================================================================================
# You can set up the tests with setup_module() & teardown_module()

# must have this exact name to use as a setup fuction
def setup_module():
    global input_4
    input_4 = 4
    print('\n----setup_module()-----')


# must have this exact name to use as a teardown fuction.  This gets called after all of the tests
def teardown_module():
    print('\n----teardown_module()------')


# ======================================================================================================================
# as an alternative to setup_module, teardown_module
# define the fixture functions in conftest.py to make them accessible across multiple test files
# ========================================= conftest.py ================================================================
@pytest.fixture
def input_value():
    print('\n----SETUP  fixture - CALL 1-----')
    yield 5  # This is passed to the functions as a parameter when called
    print('\n----TEARDOWN fixture - CALL 2 -----')  # this is invoked after tests are run
    return 

# this will set sample_data to be used for multiple tests
# scope='module' ensures that the function is only called once despite being used TWICE in this module
@pytest.fixture(scope='module')   # Possible values for scope are: 'function', 'class', 'module', 'package' or 'session'
def sample_data():   
    print('\n----sample_data fixture-----')    
    return 3    


# apply a fixture to all of the tests in a hierarchy, even if the tests don't explicitly request a fixture
@pytest.fixture(autouse=True)
def setup_dev_environment():
    pass

# Note for scope='session' the fixture must be in conftest.py file


# will run for all params
@pytest.fixture(params=["chrome", "firefox"], scope="class")
def funct():
    pass


# Note that one fixture may take anoter as a parameter
@pytest.fixture
def fix1():
    return [True, False]

@pytest.fixture
def fix2(fix1):
    return fix1[1]

# ============================================== End conftest.py =======================================================

# THIS TEST WILL PASS invoking the input_value() function and storing the yielded value
def test_method1(input_value):
    print('TESTING METHOD 1')
    print(f'You have been passed input_value=:{input_value}')
    x = input_value
    y=6
    assert x+1 == y, "test1.1 failed"
    assert y-1 == x, "test1.2 failed"
    print('end_of-test')

# THIS WILL PASS
def test_method2():
    x=5
    y=6
    assert x+1 == y, "test2.1 failed"

# THIS WILL FAIL
# pytest bezpy_90_pytest.py::test_3  will execute only this test
def test_3():
    x=5
    y=6
    assert x == y, "test3.1 failed"

# This will be ignored since function doesn't start with 'test'
def ignored_test():
    pass

# Considered a test since first 4 letters of function are 'test'
# There doesn't technically need to be an assert to be tested, will still pass
def test4():
    pass

# Test will fail and can be identified by running 'pytest -k method'
def test_method_5():
    assert 1 == 2, 'test5.1 failed'


# Test will pass and can be identified with pytest -m set1
# You can identify all others except this with pytest -m "not set1"
@pytest.mark.set1
def test_method_6():
    pass


# This tests several parameter sets
@pytest.mark.parametrize("x, y, z",[(5, 5, 10),(3, 5, 8)])
def test_method_7(x, y, z):
    assert x + y == z, "test 7.1 failed"


# Will be executed but result separated into xpassed or xfailed
@pytest.mark.xfail
def test_method_8():
    assert 15 + 13 == 29, "8.1 failed"


# This test is skipped altogether
@pytest.mark.skip('BUG_518710')  # Can pass optional string
def test_method_9():
    pass


@pytest.mark.skipif(not system() == "Windows", reason='BUG_518710')  # Conditional Test
def test_method_9b():
    pass


# TEST WILL PASS
def test_method_10(sample_data):
    assert sample_data == 3, '10.1 failed'


# TEST WILL PASS
def test_method_11(sample_data):
    assert sample_data < 5, '11.1 failed'


# TEST WILL PASS
def test_exception_1():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0
    print("EXCEPTION INFO", e_info)

# TEST WILL PASS
def test_exception_2():
    with pytest.raises(ZeroDivisionError) as exp:
        x = 1 / 0
    assert isinstance(exp.value, ZeroDivisionError)
    assert exp.value.args[0] == 'division by zero'

# TEST WILL PASS
def test_exception_3():
    with pytest.raises(ZeroDivisionError, match='division by zero'):  # your exception message must be the same as 'match'
        x = 1 / 0

# TEST WILL PASS - USES FIXTURES
def test_fix2(fix2):
    assert fix2 is False

# TEST IS FORCED TO FAIL EXPLICITLY
def test_fail():
  user_name = None
  if not user_name:
    pytest.fail('Failed to retrieve user_name')

# TEST IS FORCED TO XFAIL (ignored) EXPLICITLY
def test_xfail():
  user_name = None
  if not user_name:
    pytest.xfail()

from mylib.mymock import MyClass3

# testing with pytest using a Test Class
class TestMyPytestClass1:
    x = 3   # < -- -- treated as any static variable
    mc3 = MyClass3()

    def test_one(self):
        assert self.x == 3

    def test_two(self):
        assert self.mc3.value == 2
        assert self.mc3.method() == 3


# ======================================================================================================================
# Execute with ... pytest bezpy_90_pytest.py                ...For entire module
# Execute with ... pytest bezpy_90_pytest.py::test_fix1     ...For specific test

# FOR RESULTS  '.' = PASS  ,  'F' = FAIL, 'x' = XFAIL, 's' = SKIPPED
# .e.g bezpy_90_pytest.py ..F.F...xs.....     =>  PASS,PASS,FAIL,PASS,FAIL ...

# VERBOSE RESULTS
# bezpy_90_pytest.py::test_method1 PASSED                                                                                                                                                                                [  6%]
# bezpy_90_pytest.py::test_method2 PASSED                                                                                                                                                                                [ 13%] 
# bezpy_90_pytest.py::test_3 FAILED                                                                                                                                                                                      [ 20%]
# bezpy_90_pytest.py::test_4 PASSED                                                                                                                                                                                       [ 26%]
# bezpy_90_pytest.py::test_method_5 FAILED                                                                                                                                                                               [ 33%]
# bezpy_90_pytest.py::test_method_6 PASSED                                                                                                                                                                               [ 40%] 
# bezpy_90_pytest.py::test_method_7[5-5-10] PASSED                                                                                                                                                                       [ 46%] 
# bezpy_90_pytest.py::test_method_7[3-5-8] PASSED                                                                                                                                                                        [ 53%] 
# bezpy_90_pytest.py::test_method_8 XFAIL                                                                                                                                                                                [ 60%] 
# bezpy_90_pytest.py::test_method_9 SKIPPED                                                                                                                                                                              [ 66%] 
# bezpy_90_pytest.py::test_method_9b PASSED                                                                                                                                                                              [ 73%]
# bezpy_90_pytest.py::test_method_10 PASSED                                                                                                                                                                              [ 80%] 
# bezpy_90_pytest.py::test_method_11 PASSED                                                                                                                                                                              [ 86%] 
# bezpy_90_pytest.py::test_exception PASSED                                                                                                                                                                              [ 93%]
# bezpy_90_pytest.py::test_fix2 PASSED                                                                      [100%]
