class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        from collections import Counter

        s_chars = Counter(s)
        t_chars = Counter(t)

        if s_chars == t_chars:
            return True
        
        return False