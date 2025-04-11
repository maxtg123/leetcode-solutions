# Problem: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Solved on: 2025-04-10

import re

def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]
