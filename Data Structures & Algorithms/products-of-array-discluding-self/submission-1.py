class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            l[i] *= p
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            l[i] *= p
            p *= nums[i]
        return l