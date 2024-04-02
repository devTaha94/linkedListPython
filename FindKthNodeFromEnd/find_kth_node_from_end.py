class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

def find_kth_from_end(ll, k):
    if not ll or k < 1:  # If the list is empty or k is invalid
        return None

    slow = ll.head
    fast = ll.head

    # Move fast pointer k nodes ahead
    for _ in range(k):
        if not fast:  # If k is out of bounds
            return None
        fast = fast.next

    # print('__ ' , fast.value)
    # Move both pointers until fast pointer reaches the end
    while fast:
        slow = slow.next 
        fast = fast.next 

    return slow if slow else None


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4
"""

