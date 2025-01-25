class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        start = 0
        limit = 0

        for end in range(1, len(nums)):
            limit += (end - start) * (nums[end] - nums[end - 1])
            while start < end and limit > k:
                limit -= (nums[end] - nums[start])
                start += 1
            ans = max(ans, end - start + 1)

        return ans
