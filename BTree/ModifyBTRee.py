class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Find Node
def Find(root, x):
    if not root:
        print("The number {} is not found".format(x))
        return None
    if root.val == x:
        print("True")
        return root
    elif x < root.val:
        return Find(root.left, x)
    elif x > root.val:
        return Find(root.right, x)

# Insert Node
def BSTinsert(root, x):
    if not root:
        root = TreeNode(x)
    elif root.val > x:
        root.left = BSTinsert(root.left, x)
    elif root.val < x:
        root.right = BSTinsert(root.right, x)
    return root

# Remove Node
def Delete(root, x):
    if not root:
        raise Exception("Element not found")
    elif root.val > x:
        root.left = Delete(root.left, x)
    elif root.val < x:
        root.right = Delete(root.right, x)
    elif root.left and root.right:
        TmpCell = FindMin(root.right)
        root.val = TmpCell.val
        root.right = Delete(root.right, root.val)
    else:
        if not root.left:
            root = root.right
        else:
            root = root.left
    return root

def FindMin(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root