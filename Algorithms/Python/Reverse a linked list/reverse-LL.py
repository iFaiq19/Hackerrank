

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    if head == None:
        return None
    elif head.next == None:
        return head
    else:
        prevNode = None
        nextNode = None
        currentNode = head
    while currentNode != None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    head = prevNode
    return head
