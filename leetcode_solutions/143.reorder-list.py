# 230406

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reorderList(head):
    arr = []
    curr = head
    while curr != None:
        arr.append(curr)
        curr = curr.next
    ll_len = len(arr)
    i = 0
    if ll_len % 2 == 0:
        while i < ll_len / 2:
            arr[i].next = arr[ll_len - i - 1]
            if i == (ll_len / 2) - 1:
                arr[ll_len - i - 1].next = None
            else:
                arr[ll_len - i - 1].next = arr[i + 1]
            i += 1
    else:
        while i < (ll_len // 2) + 1:
            if i != ll_len // 2:
                arr[i].next = arr[ll_len - i - 1]
                arr[ll_len - i - 1].next = arr[i + 1]
            else:
                arr[i].next = None
            i += 1
    return
