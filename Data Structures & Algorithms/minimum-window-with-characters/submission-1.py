class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pattern = Counter(t)
        window = {}

        need = len(pattern)
        have = 0

        l = 0
        start = -1
        length = float('inf')

        for r, char in enumerate(s):
            if char in pattern:
                window[char] = window.get(char, 0) + 1
                if window[char] == pattern[char]:
                    have += 1
            
            while have == need:
                if r-l+1 < length:
                    start = l
                    length = r-l+1
                if s[l] in pattern:
                    window[s[l]] -= 1
                    if window[s[l]] < pattern[s[l]]:
                        have -= 1
                l += 1
        
        return "" if length == float('inf') else s[start:start+length]

