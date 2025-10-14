def add_logging(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f"Result of {f.__name__}({','.join(str(a) for a in args)}"
              f"{', ' if args and kwargs else ''}"
              f"{','.join(f'{k}={v}' for k, v in kwargs.items())}) is {result}")
        return result
    return wrapper


@add_logging
def f(x):
    return x**2


# f = add_logging(f)


@add_logging
def g(x, y):
    return x + y


a = f(x=3), f(2)
b = g(1, y=2)



