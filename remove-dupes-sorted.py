# LeetCode #26 - Remove duplicates from sorted array :: June 5, 2024

def RemoveDuplicates(nums: list[int]) -> int:
  if not nums:
    return []
  
  # init first pointer for unique elems
  i = 0

  for j in range(1, len(nums)):
    if nums[j] != nums[i]: # finds unique elem
      i += 1               # update index
      nums[i] = nums[j]    # update pos

  # ret num of unique
  return i + 1