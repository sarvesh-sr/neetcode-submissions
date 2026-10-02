class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0
        maxLength = 0
        for i, char in enumerate(s):
            if char in window:
                l = max(l, window[char]+1)
            window[char] = i
            maxLength = max(maxLength, i-l+1)
        return maxLength