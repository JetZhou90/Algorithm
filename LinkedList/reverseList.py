#reverse list

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

#reverse double list

def reverseDoubleList(head):
    if head == None:
        return
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        head.pre = next
        pre = head
        head = next
    return pre


# reverse Part

def reversePart(head, start, end):
    if head == None or head.next == None:
        return head
    length = 0
    pre = None
    pos = None
    node1 = head
    while node1 != None:
        length += 1
        pre = node1 if length == start-1 else pre
        pos = node1 if length == end+1 else pos
        node1 = node1.next
    if start > end or start < 1 or end > length:
        return head
    node1 = pre.next if pre != None else head
    node2 = node1.next
    node1.next = pos
    while node2 != pos:
        next = node2.next
        node2.next = node1
        node1 = node2
        node2 = next
    if pre != None:
        pre.next = node1
        return head
    return node1