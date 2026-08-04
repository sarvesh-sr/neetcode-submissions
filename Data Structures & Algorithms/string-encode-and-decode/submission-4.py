class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for i in strs:
            s.append(f"{len(i)}|{i}")
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        # 5|hello
        # 0123456
        i = 0
        l = []
        while i < len(s):
            j = i
            while s[j] != '|':
                j += 1
            n = int(s[i:j])
            a = s[j+1:j+1+n]
            l.append(a)
            i = j+1+n
        return l