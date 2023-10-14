def repeat_apply(n):
    def inner(f):
        def wrapper(x):
            result = f(x)
            for i in range(n - 1):
                result = f(result)
            return result

        return wrapper

    return inner


@repeat_apply(3)
def double(x):
    return 2 * x

# double = (repeat_apply(3))(double)


print(double(3))
