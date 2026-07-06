class Solution:
    def trap(self, height: List[int]) -> int:
        # max left and right stored as index, value
        mx_l, mx_r = height[0],height[-1]
        l,r = 0,len(height) - 1
        res = 0

        while l < r:
            if mx_l < mx_r:
                l += 1
                mx_l = max(mx_l, height[l])
                w = mx_l - height[l]
                if w > 0:
                    res += w 
            else:
                r -= 1 
                mx_r = max(mx_r, height[r])
                w = mx_r - height[r]
                if w > 0:
                    res += w
        return res