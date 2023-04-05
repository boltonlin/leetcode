# 230405

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
    # Check Nones
    if list1 == None:
        if list2 == None:
            return None
        return list2
    elif list2 == None:
        if list1 == None:
            return None
        return list1
    
    # Initialize head, tail, and ptrs
    ptr1, ptr2 = list1, list2
    if ptr1.val <= ptr2.val:
        head, tail = ptr1, ptr1
        ptr1 = ptr1.next
    else:
        head, tail = ptr2, ptr2
        ptr2 = ptr2.next

    # loop
    while ptr1 != None and ptr2 != None:
        temp1, temp2 = ptr1.next, ptr2.next

        if ptr1.val <= ptr2.val:
            tail.next = ptr1
            tail = ptr1
            ptr1 = temp1
        else:
            tail.next = ptr2
            tail = ptr2
            ptr2 = temp2

    # if anything remains, tail points to it
    if ptr1 == None:
        tail.next = ptr2
    else:
        tail.next = ptr1

    return head
