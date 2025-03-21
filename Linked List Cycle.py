class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while f and f.next:
            s, f = s.next, f.next.next
            if s == f:
                return True 
        return False
