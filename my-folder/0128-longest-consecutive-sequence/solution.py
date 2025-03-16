class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for x in nums:
            if x-1 not in nums:
                cnt = 1
                while x+1 in nums:
                    cnt += 1
                    x = x+1
                longest = max(longest,cnt)

        return longest

