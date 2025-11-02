class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merg_num = sorted(nums1 + nums2)
        n = len(merg_num)
        if n % 2 != 0:
            return merg_num[n//2]
        else:
            sum = merg_num[(n//2)-1] + merg_num[(n//2)]
            return sum/2
        
