from itertools import starmap
from collections import OrderedDict


def groupby(func, seq):
    dict_result = {}
    for element in seq:
        dict_result.setdefault(func(element), []).append(element)
    return dict_result


def iterate(func):
    def compose(outer_func, inner_func):
        return lambda arg: outer_func(inner_func(arg))

    result = lambda arg: arg
    while True:
        yield result
        result = compose(func, result)


def zip_with(func, *iterables):
    return starmap(func, zip(*iterables))


def cache(func, cache_size):

    if cache_size == 0:
        return func
    else:
        storage = OrderedDict()

        def func_cached(*args):
            if args not in storage:
                if len(storage) == cache_size:
                    storage.popitem(False)
                storage[args] = func(*args)
            return storage[args]
    return func_cached
