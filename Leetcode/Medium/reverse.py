# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example:
# Input: x = -123
# Output: -321

# Example :
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        if x > 0:
            rev = int(str(x)[::-1])
            if rev > 2147483647:
                return 0
            return rev
        if x < 0:
            x *= -1
            rev = int(str(x)[::-1]) * -1
            if rev < -2147483648:
                return 0
            return rev