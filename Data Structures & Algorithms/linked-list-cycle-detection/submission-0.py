# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = set()
        present = head

        while present:
            if present in hashmap:
                return True
            hashmap.add(present)
            present = present.next
        return False
