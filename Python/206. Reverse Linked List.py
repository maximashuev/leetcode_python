 # Given the head of a singly linked list, reverse the list, and return the reversed list.
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev