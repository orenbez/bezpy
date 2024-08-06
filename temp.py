


def sub():
    try:
        x = 1/4
    except ZeroDivisionError:
        print('ERROR1')
    else:
        print('ELSE')
        return x
    finally:
        print('fInally')

print(sub())