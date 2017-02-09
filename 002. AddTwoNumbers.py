# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        #實例化,root和n指向同一個ListNode()
        root=n=ListNode(0)
        
        while l1 or l2 or carry:
            v1=0
            v2=0
            #v是值,l是next
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            #取出除10後的商和餘,並把商加到下一輪
            carry,ans=divmod(v1+v2+carry,10)
            #把答案用n丟入ListNode()
            n.next=ListNode(ans)
            n=n.next
        return root.next
