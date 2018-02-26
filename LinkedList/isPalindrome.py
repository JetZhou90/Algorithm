
# 时间复杂度O(N)，空间复杂度O(N)

def isPalindrome1(head):
    if head == None or head.next == None:
        return True
    stack = []
    cur = head
    while cur != None:
        stack.append(cur)
        cur = cur.next
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True

# 时间复杂度O(N)，空间复杂度O(N/2)
def isPalindrome2(head):
    if head == None or head.next == None:
        return True
    stack = []
    pre = head
    cur = head
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    while pre != None:
        stack.append(pre)
        pre = pre.next
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True

# 时间复杂度O(N)，空间复杂度O(1)
def isPalindrome3(head):
    if head == None or head.next == None:
        return True
    pre = head
    cur = head
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    node = pre.next
    pre.next = None
    while node != None:
        next = node.next
        node.next = pre
        pre = node
        node = next
    node = pre
    res = True
    while pre != None and head != None:
        if pre.val != head.val:
            res = False
            break
        pre = pre.next
        head = head.next
    pre = node.next
    node.next = None
    while pre != None:
        next = pre.next
        pre.next = node
        node = pre
        pre = next
    return res


