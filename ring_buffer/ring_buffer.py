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

            if self.current and self.current is not self.storage.head:
                # Create a place to store the newly added value
                self.current.prev.value = item
                # Replace current with the new value added
                self.current = self.current.prev
            else:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
         # if self.current and self.current is not self.storage.tail:

            # if self.current == None:

            # if self.current and self.current is not self.storage.head:
            #     self.current.prev.value = item
            # self.current = self.current.prev
            # else:
            #     # if self.current and self.current is self.storage.tail:
            #     # move oldest item to end
            #     # self.storage.move_to_end(self.storage.head)
            #     # remove last item if the capacity is full
            #     self.storage.remove_from_head()
            #     # add the new item to the front
            #     self.storage.add_to_tail(item)
            #     self.current = self.storage.tail
            # elif self.current and self.current is self.storage.head:

        else:
            # add the new item if capacity is not met
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # loop through storage and insert each item into list buffer contents
        list_buffer_contents.append(self.storage.tail.value)
        node = self.storage.tail
        while node.prev is not None:

            list_buffer_contents.append(node.prev.value)
            node = node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
