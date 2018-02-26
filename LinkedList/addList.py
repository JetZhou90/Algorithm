class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

# 双栈
def addList1(head1, head2):
    if head1 == None or head2 == None:
        raise Exception("Input Error!")
    s1 = []
    s2 = []
    while head1 != None:
        s1.append(head1.val)
        head1 = head1.next
    while head2 != None:
        s2.append(head2.val)
        head2 = head2.next
    print("post")
    carry = 0
    pre = None
    while s1 or s2:
        num1 = 0 if not s1 else s1.pop()
        num2 = 0 if not s2 else s2.pop()
        sum = num1 + num2 + carry
        node = Node(sum % 10)
        node.next = pre
        pre = node
        carry = sum // 10
    if carry == 1:
        node = Node(1)
        node.next = pre
        pre = node
    return pre

# 链表逆用
def addList2(head1, head2):

    def reverseList(head):
        if head == None:
            return
        pre = None
        while head != None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    if head1 == None or head2 == None:
        raise Exception("Input Error!")
    head1 = reverseList(head1)
    head2 = reverseList(head2)
    pre1 = head1
    pre2 = head2
    pre = None
    carry = 0
    while pre1 != None or pre2 != None:
        sum = pre1.val + pre2.val + carry
        node = Node(sum % 10)
        node.next = pre
        pre = node
        carry = sum // 10
        pre1 = pre1.next
        pre2 = pre2.next
    if carry == 1:
        node = Node(1)
        node.next = pre
        pre = node
    reverseList(head1)
    reverseList(head2)
    return pre