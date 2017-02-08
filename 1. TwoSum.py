class Solution:
    def lengthOfLongestSubstring(self, s):
        start=0
        mexlen=0
        drop={}
        for i in range(len(s)):
            #查看s[i]是否在字典中而且指針在s[i]的後面
            if (s[i] in drop) and start<=drop[s[i]] :
                start=drop[s[i]]+1
            else:
                mexlen=max(mexlen,i+1-start) 
            drop[s[i]]=i
        return mexlen
