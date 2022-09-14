def try_except(x, y):
    try:
        if isinstance(y, str):
                raise TypeError("String not allowed")
        return x/y
    except ZeroDivisionError:
        print("Division by zero is not allowe")
    except TypeError as t:
        print(t)


num = try_except(4, 2)
print(num)