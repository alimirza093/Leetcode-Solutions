# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr = []
        cur = head
        # converting linkedlist in array
        while cur:
            arr.append(cur.val)
            cur = cur.next
        k = k % len(arr)
        if k == 0:
            return head
        #  rotating list
        arr = arr[-k:] + arr[:-k]
        # now convert arr into linkedlist back
        dummy = ListNode()
        temp = dummy
        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next


