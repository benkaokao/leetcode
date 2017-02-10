class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #如果只有3個直接相加
        if len(nums)==3:
            ans=nums[0]+nums[1]+nums[2]
            return ans
        if len(nums)>3:
            add=0
            diff=0
            temp={}
            sor=[]
            for each1 in range(len(nums)):
                for each2 in range(len(nums)):
                    if each1!=each2:
                        for each3 in range(len(nums)):
                            if each3!=each1 and each3!=each2:
                                #3個數先加總
                                add=nums[each1]+nums[each2]+nums[each3]
                                #取差,減掉target後取絕對值,差最小的就是答案
                                diff=abs(target-add)
                                #差當key,3個數當list(value)
                                temp[diff]=sorted([nums[each1],nums[each2],nums[each3]])
            #對差(key)進行排序                    
            sor=sorted(temp.keys())
            #把差(key)最小的值相加 
            ans=sum(temp[sor[0]])
            return ans
