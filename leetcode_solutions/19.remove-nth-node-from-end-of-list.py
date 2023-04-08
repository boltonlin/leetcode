# 230407

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(head, n):
    arr, curr = [], head
    while curr:
        arr.append(curr)
        curr = curr.next

    if len(arr) != n:
        arr[len(arr)-n-1].next = arr[len(arr)-n].next
    else:
        return arr[len(arr)-n].next
    return head

def removeNthFromEnd_alt(head, n):
    dummy = ListNode(0, head)
    l, r = dummy, head
    for i in range(n):
        r = r.next
    while r:
        l = l.next
        r = r.next
    l.next = l.next.next
    return dummy.next
