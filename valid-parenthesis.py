# LeetCode #20 - Valid Parenthesis :: June 3, 2024

# () or [] or {} = true
# [} or {) or ([)] = false

def isValid(s: str) -> bool:
  # safety! :D
  if len(s) % 2 != 0:
    return False
  if s.strip() == "":
    return False
  
  # this mess of a var dec splits the str every 2
  split_s = [s[i:i+2] for i in range(0, len(s), 2)]

  for p in split_s:
    if p not in ["()", "[]", "{}"]:
      return False
    
  return True

print(isValid("{[]}")) # t