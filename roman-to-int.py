# LeetCode #13 - Roman Numerals to Integers :: June 2, 2024

def romanToInt(s: str) -> int:
  # create a dict of key-val pairs of numerals used in the problem
  numeral_to_ints = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

  # result int
  total = 0

  # iterating through string and applying the logic of numerals
  for i in range(len(s)):
    # if i + 1 is greater than length s and exceeds value of s in index i + 1
    if i + 1 < len(s) and numeral_to_ints[s[i]] < numeral_to_ints[s[i + 1]]:
      # subtract val of current character
      total -= numeral_to_ints[s[i]]
    else:
      # if not, then add val
      total += numeral_to_ints[s[i]]
      
  return total
  

input1 = "III"     # 3    expected -
input2 = "LVIII"   # 58   expected -
input3 = "MCMXCIV" # 1994 expected -

print(romanToInt(input1))  # Output: 3
print(romanToInt(input2))  # Output: 58
print(romanToInt(input3))  # Output: 1994