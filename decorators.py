def repeat_apply(n):
    def inner(f):
        def wrapper(x):
            for i in range(n):
                x = f(x)
            return x

        return wrapper

    return inner


@repeat_apply(3)
def double(x):
    return x*2

@repeat_apply(2)
def cube(x):
    return x**3

# double = (repeat_apply(3))(double)


print(double(2))
print(cube(3))
