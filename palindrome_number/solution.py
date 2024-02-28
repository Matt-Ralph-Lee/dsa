# Palindrome Number
# Link:
# https://leetcode.com/problems/palindrome-number/?envType=featured-list&envId=top-google-questions%3FenvType%3Dfeatured-list&envId=top-google-questions

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        n = len(x_str)
        for i in range(n):
            if x_str[i] != x_str[n-1-i]:
                return False
            if i >= n-1-i:
                return True
        return False
