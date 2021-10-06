from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper_logger(arg):
        print(f'{calc_kube.__name__}({arg}: {type(arg)})')
        return func(arg)
    return wrapper_logger


@type_logger
def calc_kube(answer):
    return answer ** 3


a = calc_kube(5)
print(a)