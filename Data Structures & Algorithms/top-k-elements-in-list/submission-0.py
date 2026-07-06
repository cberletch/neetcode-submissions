class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        c = Counter(nums).most_common(k)

        return [item[0] for item in c]