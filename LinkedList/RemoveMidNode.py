import math

def removeMidNode(head):
    if head == None or head.next == None:
        return head
    if head.next.next == None:
        return head.next
    pre = head
    cur = head.next.next
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    pre.next = pre.next.next
    return head

def removeByRatio(head, a, b):
    if head == None or a < 1 or a > b:
        return head
    n = 0
    cur = head
    while cur != None:
        cur = cur.next
        n += 1
    n = math.ceil(a / b * n)
    if n == 1:
        return head.next
    cur = head
    while n-1 != 1:
        cur = cur.next
        n -= 1
    cur.next = cur.next.next
    return head