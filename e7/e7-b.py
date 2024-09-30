class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: {value} is a negative number, which is not allowed.")


def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"{number} is a positive number.")


try:
    num = -10
    check_positive_number(num)
except NegativeNumberError as e:
    print(e)
