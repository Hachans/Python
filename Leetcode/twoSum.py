# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return  [i, j]




