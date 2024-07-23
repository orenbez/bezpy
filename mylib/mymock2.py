from mylib.mymock import MyClass3  # WARNING!!!!!! needs full path mylib.mymock since my_class3 is imported from bezpy_48_unittest.py

def my_class3():
    x = MyClass3()
    return (x.value)

def test_2():
    x = MyClass3()
    return (x.method())
