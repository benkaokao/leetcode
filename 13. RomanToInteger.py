#coding:utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        ro={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        #最後一個另外算
        for i in range(len(s)-1):
            #如果前面的字比後面的字小,代表是減的
            if ro[s[i]]<ro[s[i+1]]:
                ans-=ro[s[i]]
            #不然的話,就是加的
            else:
                ans+=ro[s[i]]
        #最後一個
        ans+=ro[s[-1]]
        return ans
