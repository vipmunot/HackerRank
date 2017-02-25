"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def MergeLists(headA, headB):
    if not headA or not headB:
        head = headA or headB
        return head

    if headA.data < headB.data:
        smallerNode = headA
        smallerNode.next = MergeLists(headA.next, headB)
    else:
        smallerNode = headB
        smallerNode.next = MergeLists(headA, headB.next)

    return smallerNode  
  
  
  
