# 4Sum
# Link:
# https://leetcode.com/problems/4sum/?envType=featured-list&envId=top-google-questions%3FenvType%3Dfeatured-list&envId=top-google-questions

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)

        result = []

        for i in range(N-3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            new_target = target - nums[i]
            for j in range(i + 1, N-2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                st = j + 1
                en = N - 1
                while st < en:
                    ans = nums[j] + nums[st] + nums[en]
                    if ans == new_target:
                        result.append([nums[i], nums[j], nums[st], nums[en]])
                        st += 1
                        en -= 1
                        while st < en and nums[st] == nums[st - 1]:
                            st += 1
                        while st < en and nums[en] == nums[en + 1]:
                            en -= 1
                    elif ans < new_target:
                        st += 1
                    else:
                        en -= 1

        return result
