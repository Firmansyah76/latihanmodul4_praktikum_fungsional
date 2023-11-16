def uppercase_decorator(function):
    def wrapper():
        func_function = function()
        # make_uppercase = func_function.upper()
        return func_function.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())