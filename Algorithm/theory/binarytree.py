class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def insert(self, data):
        if self.data:
            if self.left is None:
                self.left = Node(data)
            elif self.right is None:
                self.right = Node(data)
            else:
                self.left.insert(data)
        

if __name__ == "__main__":
    root = Node(10)
    root.print_tree()