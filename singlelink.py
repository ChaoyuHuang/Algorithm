# -*- encoding: utf-8 -*-

class Node():
    """单链表的节点"""

    def __init__(self, item):
        # item 存放的元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


class SingleLinkList():
    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None，表示到达尾部
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        # 获取头指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            yield cur.item
            cur = cur.next

    def add(self, item):
        """向链表头部添加元素"""
        node = Node(item)
        # 新节点指针指向原头部节点
        node.next = self._head
        # 更新头部节点
        self._head = node

    def append(self, item):
        """向链表尾部添加元素"""
        node = Node(item)
        # 先判断链表是否为空
        if self.is_empty():
            # 空链表, _head指向新节点
            self._head = node
        else:
            # 不是空链表, 则找到尾部。将尾部节点next指向新节点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置插入节点"""
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(item)
        elif index > (self.length()):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向下一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()


if __name__ == "__main__":
    link_list = SingleLinkList()

    # 创建节点
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # 将节点添加到链表
    link_list._head = node1
    # 将第一个节点的next指针指向下一个节点
    node1.next = node2
    node2.next = node3
    link_list.insert(0, 1)
    # 访问链表
    print(link_list._head.item)
    print(link_list._head.next.item)
    print(link_list.length())
    print(link_list.items())
