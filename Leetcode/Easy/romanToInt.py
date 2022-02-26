# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# Example:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        prev = 0
        
        for i in reversed(s):
            if dict[i] >= prev:
                result += dict[i]
            if dict[i] < prev:
                result -= dict[i]
            prev = dict[i]
        return result
