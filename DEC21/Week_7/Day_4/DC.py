
#  Exceptions Write a function to compute 5/0 and use try/except to catch the exceptions.

def zero_division():
    return 5 / 0


try:
    zero_division()
except ZeroDivisionError:
    print("Error!!!!")