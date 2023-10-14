def add_logging(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f"Result of {f.__name__} is {result}")
        return result
    return wrapper


def f(x):
    return x**2


f = add_logging(f)


@add_logging
def g(x, y):
    return x + y


x = f(3), f(2)
y = g(1, 2, 3)



