# 3. Write a program to determine if a number, given on the command line, is prime.
#
#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Erathosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).

def getNum():
  # Read a number from the keyboard
  num = input("\nEnter a number: ")
  return int(num)


try:
  num = getNum()
  def printPrime(): print(f'{num} is prime.')
  def printNotPrime(): print(f'{num} is not prime.')

  if num > 1:
    for i in range(2, num//2):
      if num % i == 0:
        printNotPrime()
        print(f'{i} times {num//i} is {num}')
        break
    else:
      printPrime()
  else:
    printNotPrime()
except ValueError:
  print('It seems that you did not enter a number.')

print()
