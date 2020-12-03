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
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        node.parent = None
        self._children.remove(node)

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, node):
        if node == self._parent:
            return
        if node == None:
            self._parent = node
            return
        if self.parent:
            self._parent.remove_child(self)
        if node: 
            self._parent = node
            node.add_child(self)

    def depth_search(self, value):
        if self.value == value:
            return self
        if self.children == []:
            return None
        for child in self.children:
            search_res = child.depth_search(value)
            if search_res:
                return search_res
        return search_res
    
    def breadth_search(self, value):
        if self.value == value:
            return self
        if self.children == []:
            return None
        children = [child for child in self.children]
        while len(children):
            if children[0].value == value:
                return children[0]
            children.extend(children[0].children)
            children.pop(0)
        return None

        # for child in self.children:
        #     if child.value == value:
        #         return child


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node2
node1.parent = node3

# print(node1.children)
# print(node2.children)

print(node2.breadth_search("root2").value)
