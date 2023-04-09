# 230409

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeKLists(self, lists):
        compare = []
        empty_count = 0
        res_head, res_tail = None, None

        for i in range(len(lists)):
            compare.append(lists[i])
            if lists[i] == None:
                empty_count += 1

        idx = -2
        while empty_count < len(lists) and idx != -1:
            idx = self.find_min_idx(compare)
            if idx == -1:
                continue

            if res_head == None:
                res_head = compare[idx]
                res_tail = compare[idx]
            else:
                res_tail.next = compare[idx]
                res_tail = res_tail.next

            compare[idx] = compare[idx].next
            if compare[idx] == None:
                empty_count += 1

        return res_head

# return index of smallest value within a comparison list
    def find_min_idx(self, comparison_list):
        min = None
        res = -1
        for i, node in enumerate(comparison_list):
            if node == None:
                continue
            if min == None or node.val < min:
                min = node.val
                res = i
        return res
