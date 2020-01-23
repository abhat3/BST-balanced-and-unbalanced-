from random import sample
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVL:
    def insert(self, root, data):
        # perform BST insert
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        # update height of this node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # get balance of this node's left and right subtree
        balance = self.getBalance(root)

        # perform balancing
        if balance > 1 and data < root.left.data:
            # left left
            return self.rightRotate(root)
        elif balance < -1 and data > root.right.data:
            # right right
            return self.leftRotate(root)
        elif balance > 1 and data > root.left.data:
            # left right
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        elif balance < -1 and data < root.right.data:
            # right left
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root


    def inorder(self, root, end = " "):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end = end)
            self.inorder(root.right)

    def find(self, root, key):
        if root is None:
            return root
        if root.data == key:
            return root
        elif key < root.data:
            return self.find(root.left, key)
        else:
            return self.find(root.right, key) 

    def delete(self, root, key):
        if root is None:
            return root 
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # if only one child or no children
            # if no right child
            if root.right is None:
                temp = root.left
                root = None
                return temp
            # if no left child
            elif root.left is None:
                temp = root.right
                root = None
                return temp
            else:
            # if both children
                succParent = root.right
                succ = root.right
                while succ.left is not None:
                    succParent = succ
                    succ = succ.left
                if succParent.data == succ.data:
                    root.right = succ.right
                else:
                    succParent.left = succ.right
                root.data = succ.data
                del succ

        root.height = self.getHeight(root)

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            # left left
            return self.rightRotate(root)
        elif balance < -1 and self.getBalance(root.right) <= 0:
            # right right
            return self.leftRotate(root)
        elif balance > 1 and self.getBalance(root.left) < 0:
            # left right
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        elif balance < -1 and self.getBalance(root.right) > 0:
            # right left
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def getHeight(self, node):
        if node is None:
            return -1
        leftNodeHeight = -1 if node.left is None else node.left.height
        rightNodeHeight = -1 if node.right is None else node.right.height

        return 1 + max(leftNodeHeight, rightNodeHeight)

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def leftRotate(self, node):
        # perform rotation 
        newRoot = node.right
        temp = newRoot.left

        newRoot.left = node
        node.right = temp
        
        # update heights - Imp
        
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        return newRoot

    def rightRotate(self, node):
        newRoot = node.left
        temp = newRoot.right

        newRoot.right = node
        node.left = temp

        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        return newRoot  
    
if __name__ == "__main__":
    root = None
    newTree = AVL()
    for i in sample(range(100), 10):
        print("Inserted: ", i)
        root = newTree.insert(root, i)

    print("Inorder: ")
    newTree.inorder(root)
    print()
    print(root.data)
    toDelete = int(input("To delete: "))
    newTree.delete(root, toDelete)
    print("Inorder: ")
    newTree.inorder(root)
    print()