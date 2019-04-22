# 3. Write a program to determine if a number, given on the command line, is prime.
#
#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Erathosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).
from math import sqrt, ceil

arePrimes = [0, 1]

def primeList(end):
  start = len(arePrimes)
  for i in range(start, end+1):
    arePrimes.append(True)
  for i in range(start, ceil(sqrt(end))):
    if arePrimes[i]:
      for j in range(i*i, end+1, i):
        arePrimes[j] = False


def getNum():
  # Read a number from the keyboard
  num = input("\nEnter a number: ")
  return int(num)


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
except ValueError:
  print('It seems that you did not enter a number.')

print()
