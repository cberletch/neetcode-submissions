class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = []
        max_r = []
        min_lr = []
        
        mx_l = 0
        for num in height:
            max_l.append(mx_l)
            mx_l = max(mx_l, num)
        
        mx_r = 0
        for num in reversed(height):
            max_r.append(mx_r)
            mx_r = max(mx_r, num)

        for i in range(len(height)):
            min_lr.append(min(max_l[i],max_r[-i]))
        
        res = 0 
        for i in range(len(height)):
            if min_lr[i] - height[i] > 0:
                res += min_lr[i] - height[i]
        return res