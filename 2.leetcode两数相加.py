## 2. 两数相加 url: https://leetcode-cn.com/problems/add-two-numbers/
## code:
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2 :
            x = l1.val if l1 else 0 ## 若l1非空，则取对应的值，否则为0
            y = l2.val if l2 else 0 ## 若l2非空，则取对应的值，否则为0

            total = x + y + remainder

            curr.next = ListNode(total%10) ## 取余数
            remainder = total//10  ## 取商

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1 :
            	l1 = l1.next
            if l2 :
            	l2 = l2.next
            curr = curr.next

        if remainder :
        	curr.next = ListNode(remainder)
        return result.next