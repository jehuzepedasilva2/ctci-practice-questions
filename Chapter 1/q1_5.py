def one_away(a, b):
  '''
  There are three types of edits that can be preformed on a string: insert a character, remove a character, 
  or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
  >>> one_away('pale', 'ple')
  True
  >>> one_away('pales', 'pale')
  True
  >>> one_away('pale', 'bale')
  True
  >>> one_away('abc', 'abcc')
  False
  '''
  # ensure that string a is always the longer one
  if len(b) > len(a):
    return one_away(b, a)
  # check to see if one edit is even possible
  if len(b) < len(a)-1:
    return False
  freq = {}
  for char_a in a:
    freq[char_a] = freq.get(char_a, 0) + 1
  for char_b in b:
    if char_b in freq:
      freq[char_b] -= 1
  # check freq to make sure that at most a freq is > 0
  sum_ = 0
  for val in freq.values():
    sum_ += val
  return sum_ <= 1

# Analysis:
# Let N be the length of a, and M be the length of b
# Let K be the length of the max unique characters in a or b
# Note: K <= max(N, M)
# Time: O(max(N, M) + K) => O(max(N, M))
# Space: O(K) <= O(max(N, M)) since we use a dictionary to store the frequencies
# Note that if a, b are guaranteed to be ASCII characters then there are at most 256 characters making this
# constant space (O(1))


# THIS IS INCORRECT DOESN'T WORK FOR LAST CASE: CONSIDER 2 POINTERS
