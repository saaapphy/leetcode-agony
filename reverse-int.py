# LeetCode #7 - Reverse Integer :: June 3, 2024

# assume x86, no 64-bit anything

UPPER_LIMIT = 2147483647
LOWER_LIMIT = -2147483648

def reverse(x: int) -> int:
  # check if x is in bounds of 32-bit ints
  if x > UPPER_LIMIT or x < LOWER_LIMIT:
    raise ValueError("x is outside accepted range!")
  
  # determine sign of x
  sign = -1 if x < 0 else 1
  
  # if x is less than 0 we do some negative stripping fun
  if sign == -1:
    rev_x_str = str(x)[::-1].strip('-')
    final_rev = "-" + rev_x_str
    
    if int(final_rev) == LOWER_LIMIT:
      return 0
    else:
      return final_rev

  # if its positive we just keep vibing along
  if sign == 1:
    rev_x_str = str(x)[::-1].strip('0')
    final_rev = rev_x_str
    
    if int(final_rev) == UPPER_LIMIT:
      return 0
    else:
      return final_rev

f = reverse(int(input("int? : ")))
print(f)