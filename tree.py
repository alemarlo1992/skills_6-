"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def get_nodes(self, data):
        """ Return a list of nodes with the given data

        For example::

            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> e = Node("E")
            >>> c = Node("C", [ b1, e])
            >>> a = Node("A", [b2, c])
            >>> tree = Tree(a)
            >>> result = tree.get_nodes("B")
            >>> result == [b2, b1]
            True
            >>> tree.get_nodes("L")
            []

        """
        found_nodes = [] #create an empty list for future nodes 
        to_visit = [self.root] #start my search at the root of my tree

        while to_visit: #while loop until this condition holds
            current = to_visit.pop(0) #popping the first item of the list

            if current.data == data: #if the current data equals data im looking for 
                found_nodes.append(current) #then append to my found nodes 

            to_visit.extend(current.children) #extend my to_visit list to include next nodes
        return found_nodes #return a list of new nodes 



if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
