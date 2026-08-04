class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            if n-1 not in numset:
                c = 1
                while n+c in numset:
                    c += 1
                if c > longest:
                    longest = c
        return longest