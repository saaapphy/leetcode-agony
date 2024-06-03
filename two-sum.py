# LeetCode #1 - Two Sum :: June 1, 2024

def twoSum(nums: list[int], target: int) -> list[int]:
  num_index = {}

  for i, nums in enumerate(nums):
    complement = target - nums
    if complement in num_index:
      return [num_index[complement], i]
    num_index[nums] = i
    return []