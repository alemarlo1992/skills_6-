# Linked list with Node/LinkedList classes


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node {data}>".format(data=self.data)


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "<Linked List head={head}>".format(head=self.head)

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


def only_vowels(llist):
    """ Return a new LinkedList object containing nodes with the strings from
    the original linked list that start with vowels.

        >>> llist = LinkedList()
        >>> llist.add_node("cherry")
        >>> llist.add_node("berry")
        >>> llist.add_node("apple")
        >>> new_llist = only_vowels(llist)
        >>> new_llist.head.data == "apple"
        True
    """
    current = llist.head # set current to the head of llist
    new_llist = LinkedList() #make a new linked list that will hold nodes that start with vowels 
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    while current is not None:  
        if current.data[0] in vowels: #access the first letter of the node.data
            vowels_node = Node(current.data) #created a node object

            new_llist.add_node(current.data) #added that node to the new_llist 

        current = current.next #moves on to check the next node. 

    return new_llist
    

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
