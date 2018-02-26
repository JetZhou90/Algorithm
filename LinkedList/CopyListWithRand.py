class RandNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.rand = None

# USING HASH MAP
def copyListWithRand1(head):
    if head == None:
        return None
    map = {}
    cur = head
    while cur != None:
        map[cur] = RandNode(cur.val)
        cur = cur.next
    cur = head
    while cur != None:
        map[cur].next = None if cur.next == None else map[cur.next]
        map[cur].rand = None if cur.rand == None else map[cur.rand]
        cur = cur.next
    return map[head]

# USING COPY HEAD
def copyListWithRand2(head):
    if head == None:
        return None
    cur = head
    while cur != None:
        next = cur.next
        cur.next = RandNode(cur.val)
        cur.next.next = next
        cur = next
    cur = head
    while cur != None:
        cur.next.rand = None if cur.rand == None else cur.rand.next
        cur = cur.next.next
    copyHead = head.next
    cur = head
    while cur != None:
        next = cur.next
        cur.next = next.next
        next.next = None if next.next == None else next.next.next
        cur = cur.next
    return copyHead