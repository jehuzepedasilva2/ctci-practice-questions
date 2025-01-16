def URLfy(s, length):
  '''
  Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold
  the additional characters, and that you are given the 'true' length of the string. (Note: If implementing in Java, please use a 
  character array so that you can perform this operation in place.)
  
  >>> URLfy("Mr John Smith    ", 13)
  'Mr%20John%20Smith'
  '''
  # To run doctest: python3 -m doctest filename.py
  return '%20'.join(s.strip().split(' '))
