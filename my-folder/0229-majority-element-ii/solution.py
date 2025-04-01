class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        ans = []

        for ele in nums:
            if ele not in freq:
                freq[ele] = 1
            else:
                freq[ele] += 1

        for keys in freq:
            if freq[keys] > n/3:
                ans.append(keys)

        return ans
