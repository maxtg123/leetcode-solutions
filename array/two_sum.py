# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Solved on: 2025-04-11

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
