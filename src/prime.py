from math import sqrt, ceil, floor

arePrimes = [0, 1]

def primeList(end):
  for i in range(len(arePrimes), end+1):
    arePrimes.append(True)
  for i in range(2, ceil(sqrt(end+1)) + 1):
    if arePrimes[i]:
      for j in range(i*i, end+1, i):
        arePrimes[j] = False


def getNum():
  # Read a number from the keyboard
  num = input('\nEnter a number: ')
  return int(num)


print("\nNon-numbers, e.g. 'q', can be used to exit.")
while True:
  try:
    num = getNum()
    def printPrime(): print(f'{num} is prime.')
    def printNotPrime(): print(f'{num} is not prime.')

    if num > 1:
      if num >= len(arePrimes):
        primeList(num)
      
      if arePrimes[num]:
        printPrime()
      else:
        printNotPrime()
    else:
      printNotPrime()
    
    print()
  except ValueError:
    print('It seems that you did not enter a number.\n')
    break
