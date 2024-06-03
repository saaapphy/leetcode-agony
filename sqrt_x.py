# LeetCode #69 (nice) - Sqrt(x) :: June 2, 2024

def Sqrt(x) -> int:
  if x < 0:
    raise ArithmeticError("Sqrt of a negative is not valid!")
  if x == 0:
    return 0
  
  # inital 'guess' of sqrt
  g = x / 2
  tol = 0.01 # tol => tolerance, aka accuracy
  max_itr = 10000
  itr = 0

  while abs(g * g - x) > tol and itr < max_itr:
    g = (g + x / g) / 2
    itr += 1

  # wrapped in int() to ensure it returns closest int
  return int(g)
