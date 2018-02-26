class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


# single
def removeLastKthNode1(head, k):
    if head == None or k < 1:
        return head
    cur = head
    while cur != None:
        k -= 1
        cur = cur.next
    if k == 0:
        return head.next
    elif k < 0:
        cur = head
        while k+1 != 0:
            cur = cur.next
            k += 1
        cur.next = cur.next.next
    return head

def removeLastKthNode2(head, k):
    if head == None or k < 1:
        return head
    fast = slow = head
    while k > 0:
        k -= 1
        if fast == None:
            return head
        else:
            fast = fast.next
    if fast == None:
        return head.next
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

# double

class DoubleNode:
    def __init__(self, val = None):
        self.val = val
        self.pre = None
        self.next = None

def removeLastKthDoubleNode1(head, k):
    if head == None or k < 1:
        return head
    cur = head
    while cur != None:
        k -= 1
        cur = cur.next
    if k == 0:
        head = head.next
        head.pre = None
    elif k < 0:
        cur = head
        while k+1 != 0:
            k += 1
            cur = cur.next
        cur.next = cur.next.next
        if cur.next != None:
            cur.next.pre = cur
    return head

def removeLastKthDoubleNode2(head, k):
    if head == None or k < 1:
        return head
    fast = slow = head
    while k > 0:
        k -= 1
        if fast != None:
            fast = fast.next
        else:
            return head
    if fast == None:
        head = head.next
        head.pre = None
    else:
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        if slow.next != None:
            slow.next.pre = slow
    return head