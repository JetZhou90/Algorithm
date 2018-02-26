def listPartition(head, pivot):
    def partition(nodeArr, pivot):
        left = -1
        right = len(nodeArr)
        index = 0
        while index < right:
            if nodeArr[index].val < pivot:
                left += 1
                nodeArr[left], nodeArr[index] = nodeArr[index], nodeArr[left]
                index += 1
            elif nodeArr[index].val == pivot:
                index += 1
            else:
                right -= 1
                nodeArr[index], nodeArr[right] = nodeArr[right], nodeArr[index]


    if head == None or head.next == None:
        return head
    cur = head
    n = 0
    while cur != None:
        n += 1
        cur = cur.next
    nodeArr = []
    cur = head
    while cur != None:
        nodeArr.append(cur)
        cur = cur.next
    partition(nodeArr, pivot)
    for i in range(n-1):
        nodeArr[i].next = nodeArr[i+1]
    nodeArr[-1].next = None
    return nodeArr[0]


## 进阶问题
def listPartition2(head, pivot):
    if head == None or head.next == None:
        return head
    sH = None    #small部分的头
    sT = None    #small部分的尾
    eH = None    #equal部分的头
    eT = None    #equal部分的尾
    bH = None    #big部分的头
    bT = None    #big部分的尾
    while head != None:
        next = head.next
        head.next = None
        if head.val < pivot:
            if sH == None:
                sH = head
                sT = head
            else:
                sT.next = head
                sT = head
        elif head.val == pivot:
            if eH == None:
                eH = head
                eT = head
            else:
                eT.next = head
                eT = head
        else:
            if bH == None:
                bH = head
                bT = head
            else:
                bT.next = head
                bT = head
        head = next
    head = None
    if sT != None:
        head = sH
        if eH != None:
            sT.next = eH
        elif bH != None:
            sT.next = bH
    if eT != None:
        head = head if head != None else eH
        if bH != None:
            eT.next = bH
    return head