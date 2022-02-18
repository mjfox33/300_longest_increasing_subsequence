class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        #base cases
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1
        # dynamic programmig code
        dp = [1] * n
        dp[0] = 1
        dp[1] = 2 if nums[1] > nums[0] else 1
        p0 = 0
        for i in range(2,n):
            p0 = i-2
            max_increasing = dp[i-1] if nums[i] > nums[i-1] else 0
            while p0 >= 0:
                if nums[i] > nums[p0]:
                    max_increasing = max(max_increasing, dp[p0])
                p0 -= 1
            if max_increasing > 0:
                dp[i] = max_increasing + 1
        return max(dp)