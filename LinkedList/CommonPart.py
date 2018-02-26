class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def printCommonPart(head1, head2):
    if head1 == None or head2 == None:
        return
    print("Common Part:", end=' ')
    while head1 != None and head2 != None:
        if head1.val > head2.val:
            head2 = head2.next
        elif head1.val < head2.val:
            head1 = head1.next
        else:
            print(head1.val, end=' ')
            head1 = head1.next
            head2 = head2.next
    print()


