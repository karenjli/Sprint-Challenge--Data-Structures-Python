from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check if the capacity is full, if yes, pop off the last item
        # Append the item
        if self.storage.length == self.capacity:
            # save next delete value

            # move oldest item to end
            self.storage.move_to_end(self.storage.head)
            # remove last item if the capacity is full
            self.storage.remove_from_tail()
            # add the new item to the front
            self.storage.add_to_head(item)
        else:
            # add the new item if capacity is not met
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # loop through storage and insert each item into list buffer contents
        list_buffer_contents.append(self.storage.head.value)
        node = self.storage.head
        while node.next is not None:

            list_buffer_contents.append(node.next.value)
            node = node.next

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
