class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        nums=nums[::-1]
        nu=set(nums)
        for i in nums:
            if -i in nu:
                return i
        return -1