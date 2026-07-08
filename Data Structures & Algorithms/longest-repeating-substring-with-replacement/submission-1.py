class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = set()
        res,left,right = 0,0,1
        burn = k

        while left < len(s):
            if s[left] not in st:
                st.add(s[left])
                cur_max = 1
            
            if right < len(s) and s[right] in st:
                 cur_max += 1
                 right += 1
                 res = max(res, cur_max)
            elif burn > 0 and res < len(s):
                burn -= 1
                cur_max += 1
                right += 1
                res = max(res, cur_max)
            else: 
                st.remove(s[left])
                left += 1
                right = left + 1
                res = max(res, cur_max)
                burn = k

        return res