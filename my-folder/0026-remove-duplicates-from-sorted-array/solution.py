class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uni = []
        j = 0
        for ele in nums:
            if ele not in uni:
                uni.append(ele)
                nums[j] = ele
                j += 1

        return len(uni)
