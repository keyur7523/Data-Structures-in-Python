class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def search(self, val):
        if self.data == val:
            return True      
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False           
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.data and not self.left:
            return self.data      
        if self.left:
            return self.left.find_min()

    def find_max(self):
        if self.data and not self.right:
            return self.data     
        if self.right:
            return self.right.find_max()
     
    def calculate_sum(self):
        sum = 0
        sum += self.data
        if self.left:
            sum += self.left.calculate_sum()      
        if self.right:
            sum += self.right.calculate_sum()       
        return sum
   
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
    #        min_val = self.right.find_min()
    #        self.data = min_val
    #        self.right = self.right.delete(min_val)
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self
    
    def height_tree(self):
        if self.left is None and self.right is None:
            return 0
        else:
            if self.left and self.right:
                return max(self.left.height_tree(), self.right.height_tree()) + 1
            if self.left:
                return self.left.height_tree() + 1
            if self.right:
                return self.right.height_tree() + 1
            
    def is_balanced(self):
        while self.left is not None or self.right is not None:
            if abs(self.left.height_tree() - self.right.height_tree()) > 1:
                return False
        return True

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
     
#                                   5
#                                 3   6
#                              1    4     7
#                                           8
#                                               9
#                        

if __name__ == "__main__":
    numbers = [9, 7, 21, 5, 8, 13, 27, 1, 6, 25, 35, 28, 36]
    numbers_tree = build_tree(numbers)
    #print(f'Preorder Traversal: {numbers_tree.pre_order_traversal()}')
    #print(f'Inorder Traversal: {numbers_tree.in_order_traversal()}')
    #print(f'Postorder Traversal: {numbers_tree.post_order_traversal()}')
#    print(numbers_tree.search(2))
    #print(f'Minimum element in tree: {numbers_tree.find_min()}')
    #print(f'Maximum element in tree: {numbers_tree.find_max()}')
    #print(f'Sum of all the elemnts in tree: {numbers_tree.calculate_sum()}')
    #print(f'height of the tree: {numbers_tree.height_tree()}')
    #x = 3
    #numbers_tree.delete(x)      
    #print(f'Tree after deletion of {x}: {numbers_tree.in_order_traversal()}')
   
    print(f'Is balanced: {numbers_tree.is_balanced()}')