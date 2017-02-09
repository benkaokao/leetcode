# coding:utf-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
         [   1   5   9
             2 4 6 8 10
           ] 3   7   11
        """
        #如果長度是1,或是字串比長度短,直接回傳字串
        if numRows==1 or numRows>=len(s):
            return s
        L=[""]*numRows
        index=0
        stpe=1
        for i in s:
            L[index]+=i
            #如果數到底就往上數
            if index==numRows-1:
                stpe=-1
            #如果屬到頂就往下數
            elif index==0:
                stpe=1
            index+=stpe
        return ''.join(L) 
