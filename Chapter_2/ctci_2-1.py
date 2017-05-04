class LinkedList(object):
    """Singly-Linked list"""

    def __init__(self, values=None):
        """Set up list with optional starting data"""

        self.head = None

    def add_node(self, node):
        """Add node to the linked list"""

        if self.head is None:
            self.head = node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = node


class Node(object):
    """Linked list node"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_duplicates(linked_list):
    """Remove duplicates from an unsorted linked list"""

    node_values = set()

    prev = None
    curr = linked_list.head

    while curr is not None:
        if curr.data in node_values:
            curr = curr.next
            prev.next = curr

        else:
            node_values.update(curr.data)
            prev = curr
            curr = curr.next
