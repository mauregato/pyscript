#prueba
__author__ = 'david'
def cube(number):
    number = number * number * number
    return number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False