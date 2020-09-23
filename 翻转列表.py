# encoding:utf-8

# 迭代写法
## 迭代方法，通过声明一个头指针进行节点与节点之间的链接
class Solution(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(self, head):
    headNode = ListNode(0)
    while head is not None:
        temp = head.next
        head.next = headNode.next
        headNode.next = head
        head = temp
    return headNode.next


## 利用中间变量
##时间复杂度O(N)
##空间复杂度O(1)
class Solution(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


##  递归

##时间复杂度O(N)
##空间复杂度O(1)
class Solution(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def reverseList(self, head):
        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextNode
