class Tree(object):
    def __init__(self, name = 'root', childern = None):
        self.data = None
        self.chilern = []
        if childern is not None:
            for child in childern:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
root = Tree()
root.data = "root"

print(root.data)