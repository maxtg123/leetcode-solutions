# Problem: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Solved on: 2025-04-11

def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b
