class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        rn=[]
        ans=0
        #把兩個陣列相加
        rn=nums1+nums2
        #排序
        rn=sorted(rn)
        rn_len=len(rn)
        #取中間的值
        if rn_len%2==0:
            rn=rn[(rn_len//2-1):(rn_len//2)+1]
        else:
            rn=rn[rn_len//2:rn_len//2+1]
        #值相加
        for each in rn:
            ans+=each
        rn_len=len(rn)
        #算平均
        ans=ans/rn_len
        
        return ans
