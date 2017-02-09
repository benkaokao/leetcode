import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #使用爬蟲搜尋str.strip(),找字串是'[+-]?[0-9]+'
        str=re.match('[+-]?[0-9]+',str.strip())
        #沒有的話,返回0
        if not str:
            return 0
        #找到的字串,轉成int
        str=int(str.group())
        if str>2147483647:
            return 2147483647
        elif str<-2147483648:
            return -2147483648
        else:
            return str
