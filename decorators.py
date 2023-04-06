def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("Hello world")


@greet
def add(a, b):
    print(a + b)


# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)


# it can be used as cache alsp

def cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



# The logging module is used to create log messages. It provides a set of functions that
# can be used to log messages of different levels of severity, such as info(), warning(),
# error(), and critical(). In this case, the info() function is used to log information about the function calls.


import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b