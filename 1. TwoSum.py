class Solution(object):
    def twoSum(self, nums, target):
        
        buss={}
        if nums>=2:
            for i in range(len(nums)):
                #如果nums[i]在字典裏面,就是答案,返回答案
                if nums[i] in buss:
                    return [buss[nums[i]],i]
                #拿nums[i]減去答案的值,存入字典,如果有值符合那就是答案
                else:
                    buss[target-nums[i]]=i
