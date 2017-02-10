class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #如果是輸入空,回傳""
        if not strs:
            return ""
        #如果只輸入1個字串,直接回傳字串
        if len(strs)==1:
            return strs[0]
        
        #找出所有字串的最小長度
        minl=min([len(i) for i in strs])
        
        #只比對最小字串長度,i=每個字元
        for i in range(minl):
            #依序拿出字元做比較,j=每個字串
            for j in range(1,len(strs)):
                #比較每一個字串相對的字是否一樣
                if strs[j][i]!=strs[j-1][i]:
                    #只要比到不一樣就回傳前面的字串
                    return strs[0][:i]
        
        #都一樣,回傳整串字串(最小長度)     
        return strs[0][:minl]
