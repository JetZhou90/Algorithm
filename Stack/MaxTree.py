class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def getMaxTree(arr):
    nArr = [Node(arr[i]) for i in range(len(arr))]
    lBigMap = {}
    rBigMap = {}
    stack = []
    for i in range(len(nArr)):
        curNode = nArr[i]
        while stack and stack[-1].value < curNode.value:
            cur = stack.pop()
            lBigMap[cur] = stack[-1] if stack else None
            rBigMap[cur] = curNode
        stack.append(curNode)
    while stack:
        cur = stack.pop()
        lBigMap[cur] = stack[-1] if stack else None
        rBigMap[cur] = None
    head = None
    for i in range(len(nArr)):
        curNode = nArr[i]
        left = lBigMap[curNode]
        right = rBigMap[curNode]
        if left == None and right == None:
            head = curNode
        elif left == None:
            if right.left == None:
                right.left = curNode
            else:
                right.right = curNode
        elif right == None:
            if left.left == None:
                left.left = curNode
            else:
                left.right = curNode
        else:
            parent = left if left.value < right.value else right
            if parent.left == None:
                parent.left = curNode
            else:
                parent.right = curNode

    return head

getMaxTree([2,3,4,1,5,6])