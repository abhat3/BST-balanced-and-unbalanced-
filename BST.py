from random import sample
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def inorder(self, root, end = " "):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end = end)
            self.inorder(root.right)
    
    def delete(self, root, key):
        if root is None:
            return root
        
        if key < root.data:
            root.left = self.delete(root.left, key)
            return root
        elif key > root.data:
            root.right = self.delete(root.right, key)
            return root
        else:
            # if key matches
            # if only one child, then promote it to the current node's place
            if root.left is None:
                temp = root.right 
                del root
                return temp
            elif root.right is None:
                temp = root.left
                del root
                return temp
            # if both children, then find the inorder successor in the right subtree
            else:
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
                return root

        

if __name__ == "__main__":
    root = None
    newTree = BST()
    for i in sample(range(100), 4):
        print("Inserted: ", i)
        root = newTree.insert(root, i)

    print("Inorder traversal: ")
    newTree.inorder(root)
    print()
    toDelete = int(input("Enter a valid node to delete: "))
    root = newTree.delete(root, toDelete)
    print("Inorder traversal: ")
    newTree.inorder(root)
    print()
