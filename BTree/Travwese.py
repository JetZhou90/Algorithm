class TreeNode:
    def __init__(self, x):
        root.val = x
        root.left = None
        root.right = None


# Create Tree
def create_tree(root):
    element = input("Enter a key: ")
    if element == '#':
        root = None
    else:
        root = TreeNode(element)
        root.left = create_tree(root.left)
        root.right = create_tree(root.right)
    return root

# Recurion
def pre_order(root):
    if root:
        print(root.val,end=' ')
        pre_order(root.left)
        pre_order(root.right)

def mid_order(root):
    if root:
        mid_order(root.left)
        print(root.val, end=' ')
        mid_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=' ')

# Non Recurion with Stack
def preorder(root):
    if not root:
        return
    stack = []
    while root or len(stack):
        if root:
            stack.append(root)
            print(root.val, end=' ')
            root = root.left
        else:
            root = stack.pop()
            root = root.right

def midorder(root):
    if not root:
        return
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val, end=' ')

            root = root.right
            
## Two Stacks
def postorder(root):
    if not root:
        return
    stack1 = []
    stack2 = []
    while root or stack1:
        if root:
            stack1.append(root)
            stack2.append(root.val)
            root = root.right
        else:
            root = stack1.pop()
            root = root.left
    while stack2:
        print(stack2.pop(), end=' ')

## One Stack
def postOrder(root):
    if not root:
        return
    stack = []
    stack.append(root)
    c = None
    while stack:
        c = stack[-1]
        if c.left and c.left != root and c.right != root:
            stack.append(c.left)
        elif c.right and c.right != root:
            stack.append(c.right)
        else:
            print(stack.pop().val, end=' ')
            root = c

