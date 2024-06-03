# LeetCode #3110 - Score of String :: June 3, 2024

"""

You are given a string s. The score of a string is defined as
the sum of the absolute difference between the ASCII values of adjacent characters.

"""

def ScoreOfString(s: str) -> int:
  ascii_score = 0
  for i in range(len(s) - 1):
    ascii_score += abs(ord(s[i]) - ord(s[i + 1]))
  return ascii_score


sample = 'zaz'
print(ScoreOfString(sample))