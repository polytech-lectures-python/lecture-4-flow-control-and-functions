def composition(*funcs):
    def composition_fun(data):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return composition_fun


f = composition(lambda x: x**2, lambda x: 2 * x, lambda x: x + 1)
print([f(x) for x in range(10)])
