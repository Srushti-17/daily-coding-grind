class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
                nums[j] = nums[i]
                j += 1
        k = len(nums) - len(temp)
        for l in range(k,0,-1):
            nums[-l] = 0
