# Reverse Integer
# Link:
# https://leetcode.com/problems/reverse-integer/?envType=featured-list&envId=top-google-questions%3FenvType%3Dfeatured-list&envId=top-google-questions

class Solution:
    def reverse(self, x: int) -> int:
        result = ""
        if x < 0:
            result = "-"
            x = x * -1
        x_str = str(x)
        n = len(x_str)
        for i in range(n):
            result = result + x_str[n-1-i]
        result = int(result)
        if result > (2**31) - 1 or result < -1*(2**31):
            return 0
        return result
