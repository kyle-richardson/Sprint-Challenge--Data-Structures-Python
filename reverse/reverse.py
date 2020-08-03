class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def length(self):
        count = 0
        if self.head == None:
            return 0
        else:
            p = self.head
            while p is not None:
                count += 1
                p = p.get_next()
            return count

    def reverse_list(self, node, prev):
        count = 0
        p = self.head
        while p is not None:
            self.add_to_head(p.value)
            p = p.get_next()
            if count == 0:
                self.head.set_next(None)
            count += 1
