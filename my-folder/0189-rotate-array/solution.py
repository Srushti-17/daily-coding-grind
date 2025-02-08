class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0: 
            return

        temp = nums[-k:] + nums[:-k]
        for i in range(len(temp)):
            nums[i] = temp[i]
