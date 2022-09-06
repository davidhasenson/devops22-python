# Skriv ett program (med for-loop) som skriver ut följande:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

x = 0
for x in range(10):
    print(str(x) * x)
