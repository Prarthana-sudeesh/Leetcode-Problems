
#class ListNode(object):
    #def __init__(self, val=0, next=None):
       # self.val = val
       # self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #:type l1: Optional[ListNode]
        #:type l2: Optional[ListNode]
        #:rtype: Optional[ListNode]

        list1=[]
        list2=[]
        current=l1
        number1=""
        while current:
            list1.append(current.val)
            number1 = str(current.val) + number1
            current = current.next
        current2=l2
        number2=""
        while current2:
            list2.append(current2.val)
            number2 =str(current2.val) + number2
            current2 = current2.next
        number3 = int(number1) + int(number2)
        digits = str(number3)
        head = ListNode(int(digits[-1]))
        current = head

        for i in range(len(digits) - 2, -1, -1):
            current.next = ListNode(int(digits[i]))
            current = current.next

        return head

        