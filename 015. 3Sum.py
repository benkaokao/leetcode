class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        for each1 in range(len(nums)):
            for each2 in range(len(nums)):
                if each1!=each2:
                    for each3 in range(len(nums)):
                        if each3!=each1 and each3!=each2:
                            if nums[each1]+nums[each2]+nums[each3]==0:
                                #排序
                                temp=sorted([nums[each1],nums[each2],nums[each3]])
                                #不重複就加入
                                if temp not in ans:
                                    ans.append(temp)
                                
        return ans
