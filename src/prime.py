from math import sqrt, ceil, floor

arePrimes = [0, 1]

def primeList(end):
  start = len(arePrimes)
  for i in range(start, end+1):
    arePrimes.append(True)
  start = floor(sqrt(start)) // 2 - 1
  if start < 2: start = 2
  for i in range(start, ceil(sqrt(end)) + 1):
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
