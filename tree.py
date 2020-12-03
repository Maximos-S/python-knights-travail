class Node():
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []
    
    @property
    def value(self):
        return self._value
    
    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            node.parent = self._value
            self._children.append(node)

    def remove_child(self, node):
        node.parent = None
        self._children.remove(node)

    @property
    def parent(self):
        return self._parent
    