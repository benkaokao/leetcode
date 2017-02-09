class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        #比對相反後是否相同
        x=str(x)
        if x[:]==x[::-1]:
            return True
        else:
            return False
