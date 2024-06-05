# LeetCode #12 - Integer to Roman :: June 4, 2024

def intToRoman(num: int) -> str:
  # giant ahh tuple list with numerals and numbers
  val_to_numeral = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
  ]

  numeral_result = ""

  # itr over each val and num pair
  for value, numeral in val_to_numeral:
    while num >= value:
      numeral_result += numeral
      num -= value
    
  return str(numeral_result)