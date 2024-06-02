# LeetCode #344 - Reverse String :: June 2, 2024

# to reverse a string, you must modify the input array in-place with 0(1) extra memory

def reverseString(s: list[str]) -> None:
  # initalize pointers at the start and end of the array
  left = 0
  right = len(s) - 1

  # loop to swap elements until left == right
  while left < right:
    # this swaps the elements from L-R to R-L
    s[left], s[right] = s[right], s[left]

    # advance and subtract pointers 1 closer
    left += 1
    right -= 1

s1 = ["h", "e", "l", "l", "o"]
reverseString(s1)
print(s1)  # Output: ['o', 'l', 'l', 'e', 'h']

s2 = ["H", "a", "n", "n", "a", "h"]
reverseString(s2)
print(s2)  # Output: ['h', 'a', 'n', 'n', 'a', 'H']