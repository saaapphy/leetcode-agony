# LeetCode #9 - Palindrome Number :: June 2, 2024

def IsPalindrome(x: int):
  # throw false on all negatives
  if x <= 0:
    return False
  
  # conv to str, slice -1 and compare
  if str(x) == str(x)[::-1]:
    return True
  else:
    return False


  
aa = 121
bb = -121
cc = 10

print(IsPalindrome(aa))
print(IsPalindrome(bb))
print(IsPalindrome(cc))
