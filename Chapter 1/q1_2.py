def check_permutation(a, b):
  '''
    Check Permutation: Given two strings, write a method to decide if one is a permutation of
    of the other.
  '''
  if len(a) != len(b):
    return False
  frequencies = {}
  for char in a:
    frequencies[char] = frequencies.get(char, 0)+1
  for char in b:
    frequencies[char] = frequencies.get(char, 0)-1
  for val in frequencies.values():
    if val < 0 or val > 0:
      return False
  return True

# Analysis: 
# Let A be the length of string a, B the length of string b. Since A = B will let N be the length
# We iterate over a and b to place in the dictionary. Then we iterate over the values in frequencies
# Time: O(N)
# We store the characters in both a and b in frequencies which is constant since there are a finite number of characters
# Space: O(C), where C is the size of the character set (e.g., 128 for ASCII or 256 for extended ASCII).


