__author__ = 'guodl'


a = "test"

def test_function():
    a = 23
    print a

def test_function2():
    global a

    a = 43
    print a



test_function()
print a

test_function2()

print a


def func (v, a=[]):
    a.append(v)
    return  a


if __name__ == "main":

    a = func(1)

    print a




