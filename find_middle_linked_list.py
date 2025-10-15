class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = fast = head
    while fast and fast.next:  # ✅ Handles all cases
        slow = slow.next
        fast = fast.next.next
    return slow.data


# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
print(find_middle(head))
