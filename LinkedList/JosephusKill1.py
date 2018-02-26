def josephusKill1(head, m):
    if head == None or head.next == None or m < 1:
        return head
    pre = head
    while pre.next != head:
        pre = pre.next
    count = 1
    while head != pre:
        if count != m:
            head = head.next
            pre = pre.next
            count += 1
        else:
            pre.next = head.next
            head = pre.next
            count = 1
    return head


def josephusKill2(head, m):
    def getLive(n, m):
        if n == 1:
            return 1
        return (getLive(n-1, m) + m - 1) % n + 1

    if head == None or head.next == None or m < 1:
        return head
    n = 1
    cur = head
    while cur.next != head:
        n += 1
        cur = cur.next
    n = getLive(n, m)
    while n-1 != 0:
        n -= 1
        head = head.next
    head.next = head
    return head