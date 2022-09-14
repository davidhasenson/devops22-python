def is_float(x):
    if isinstance(x, float):
        print("Är en float")
        #pass
    else:
        raise TypeError("Är inte en float")

#is_float(2)
is_float(2.0)

#print(2 == float)

