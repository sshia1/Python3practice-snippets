"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Found = False
        i1 = 0;
        while not(Found) and (i1 < len(nums)):
            i2 = i1 + 1;
            while not(Found) and (i2 < len(nums)):
                  curTarget = nums[i1]+nums[i2]
                  if (curTarget == target):
                     Found = True
                  else:
                     i2 = i2 + 1
            if not(Found):
                i1 = i1 + 1
        return[i1,i2]
