# Skriv ett program som använder sig av nästlade while-loopar för att skriva ut alla primtal
# som är mindre än 100.
# Vägledning: Primtal är ett tal som är större än 1 och som inte går att dela jämnt med
# något tal annat än sig själv och 1 . Se wikipedia för hur man kan beräkna vad som är ett
# primtal: https://sv.wikipedia.org/wiki/Primtal
# Exempel på primtal är 2, 3, 5, 7, 11, 13, 17 och 19
# 4, 6, 8, 9, 10, 12, 14, 15, 18 och 20 är inte primtal (eftersom t.ex. 20/ 5 = 4, 14/7 = 2 osv)


prime_numbers = []
x = 1

#while x >= 1:
 
while x < 100:
    prime = True
    y = 2
    if y <= x:
    #if y < x:
        #print(x)
        #print(y)
        while x % y == 0:
            #print(f"{x} break")
            prime = False
            break
        y += 1
    if prime == True:
        prime_numbers.append(x)
    x += 1
print(prime_numbers)

myPrimeNumbers = []
i = 1
while i <= 10:

  if i > 1:
    isPrime = True
  else:
    isPrime = False

  j = 2
  while j < i:
    if i%j == 0:
      isPrime = False
      break
    j += 1

  if isPrime:
    print(i, "is a prime number")
    myPrimeNumbers.append(i)
  else:
    print(i)

  i += 1

print(myPrimeNumbers)