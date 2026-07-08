class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        max_count = 0
        res,left= 0,0
        
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1

            max_count = max(max_count, counter[s[right]])

            while (right - left + 1) - max_count > k:
                counter[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res
        