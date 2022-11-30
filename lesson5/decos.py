import random
import traceback
from datetime import datetime
from time import sleep

TAX_CONSTANT = 0.1

""" builtins - all places in the python world
    -- module - all objects declared/imported above
        -- func - all objects inside the function
            -- func in func - all object inside the func in func
"""


def tax_applied(tax_size):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs): # -> result
            result = func(*args, **kwargs)
            return result - result * tax_size
        return wrapper
    return outer_wrapper


@tax_applied(TAX_CONSTANT)
def calculate_salary(salary_p_day, days):
    return salary_p_day * days


def execute_time(func):
    def wrapper(*args, **kwargs):
        before = datetime.now()
        result = func(*args, **kwargs)
        after = datetime.now()
        print(f"Execution time: {(after - before).seconds} s")
        return result

    return wrapper


def logger_boy(func):
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as err:
            with open("logs.txt", "a+") as fp:
                fp.write(traceback.print_exc())
        return result

    return wrapper


@execute_time
def random_sleeper():
    sleep(random.randint(1, 10))
    print("epwrouwprouw")


if __name__ == '__main__':
    print(calculate_salary(30, 18))
    pass
    for x in range(3):
        random_sleeper()
