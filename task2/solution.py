from collections import OrderedDict


def groupby(func, seq):
    dict_result = {}
    for elem in seq:
        dict_result.setdefault(func(elem), []).append(elem)
    return dict_result


def iterate(func):
    f = lambda x: x
    compose = lambda y: lambda x: func(y(x))
    while True:
        yield f
        f = compose(f)


def zip_with(func, *iterables):
    return [func(*args) for args in zip(*iterables)]


def cache(func, cache_size):

    stored = OrderedDict()

    def func_cached(arg):
        if arg not in stored:
            result=func(arg)
            if len(stored) == cache_size:
                stored.popitem(False)
            stored[arg] = result
            return result
    return func_cached
