class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return "Invalid number of arguments"


calc = Calculator()

result1 = calc.add(10, 20)
print("Sum of 10 and 20:", result1)

result2 = calc.add(10, 20, 30)
print("Sum of 10, 20 and 30:", result2)

result3 = calc.add(10)
print(result3)
