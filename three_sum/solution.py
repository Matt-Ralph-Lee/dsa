# 3Sum
# Link:
# https://leetcode.com/problems/3sum/?envType=featured-list&envId=top-google-questions%3FenvType%3Dfeatured-list&envId=top-google-questions

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        N = len(nums)

        for i in range(N):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            st = i + 1
            en = N - 1
            while st < en:
                ans = nums[i] + nums[st] + nums[en]
                if ans == 0:
                    result.append([nums[i], nums[st], nums[en]])
                    st += 1
                    en -= 1
                    while st < en and nums[st] == nums[st - 1]:
                        st += 1
                    while st < en and nums[en] == nums[en + 1]:
                        en -= 1
                elif ans < 0:
                    st += 1
                    # while st < en and nums[st] == nums[st - 1]:
                    #     st += 1
                else:
                    en -= 1
                    # while st < en and nums[en] == nums[en + 1]:
                    #     en -= 1

        return result
