class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        res = 0
        left = 0

        for char in s:

            while char in st:
                st.remove(s[left])
                left +=1
            
            st.add(char)
            res = max(res, len(st))

        return res