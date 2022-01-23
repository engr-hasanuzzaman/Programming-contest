class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

class Solution:
    def insertToAVL(self, root, key):
        # first node
        if not root:
            return Node(key)
        
        # BST insertion
        if key > root.data:
            root.right = self.insertToAVL(root.right, key)
        elif key < root.data:
            root.left = self.insertToAVL(root.left, key)

        root.height = self.calHeight(root)
        balance = self.getHeight(root.left) - self.getHeight(root.right)
        
        # LeftLeft: left tree heigh is 2 more heigher thant right tree
        # need to to right rotation
        if balance > 1 and key < root.left.data:
            return self.rightRotation(root)
        elif balance < -1 and key > root.right.data:
            return self.leftRotation(root)
        # LR
        elif balance > 1 and key > root.left.data:
            # perform left rotation to prepare for right rotation
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        elif balance < -1 and key < root.right.data:
            # perform right rotation to prepare for left rotation
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)
    
        return root
    def getHeight(self, node):
        if not node:
            return 0
            
        return node.height
    
    def rightRotation(self, root):
        newRoot = root.left
        t3 = newRoot.right
        # rotation
        newRoot.right = root
        root.left = t3
        
        # first update height of root then new root
        root.height = self.calHeight(root)
        newRoot.height = self.calHeight(newRoot)

        return newRoot
        
    def leftRotation(self, root):
        newRoot = root.right
        t3 = newRoot.left
        # rotation
        newRoot.left = root
        root.right = t3
    
        # update height
        root.height = self.calHeight(root)
        newRoot.height = self.calHeight(newRoot)
    
        return newRoot
        
    def calHeight(self, root):
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def preTraversal(self, root):
        if not root:
            return ''
        self.preTraversal(root.left)
        self.preTraversal(root.right)