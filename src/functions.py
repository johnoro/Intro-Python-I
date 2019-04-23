# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
  return num % 2 == 0


def getNum():
  # Read a number from the keyboard
  num = input('Enter a number: ')
  return int(num)


try:
  num = getNum()
  # Print out "Even!" if the number is even. Otherwise print "Odd"
  # YOUR CODE HERE
  print('Even' if is_even(num) else 'Odd')
except:
  print('That is odd, but not quite odd in terms of numbers.')
  print('It seems that you did not enter a number.')
