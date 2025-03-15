class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = [], []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        j = 0
        for i in range(n):
            if i% 2 == 0:
                nums[i] = pos[j]
            else:
                nums[i] = neg[j]
                j += 1

        return nums
