# coding:utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #把x轉成字串
        x=str(x)
        #如果x的開頭是"-","-"後面的數字翻轉
        if x[0]=='-':
            x=x[0]+x[-1:0:-1]
        #正數直接翻轉
        else:
            x=x[::-1]
        #轉回數字
        x=int(x)
        #超過32位元,回0,不然回x
        if abs(x)>0x7FFFFFFF:
            return 0
        else:
            return x
