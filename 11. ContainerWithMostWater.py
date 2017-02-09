class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans=0
        vol=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                #找兩個數最小的當高,在乘以兩個數之間的距離
                vol=min(height[i],height[j])*(j-i)
                #找出最大的答案
                ans=max(ans,vol)
        return ans      
