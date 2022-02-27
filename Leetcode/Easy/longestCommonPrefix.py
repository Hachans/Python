# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        prefix = ""
        for x, y in zip(min(strs), max(strs)):
            if x == y:
                prefix += x
            else:
                break
        return prefix
