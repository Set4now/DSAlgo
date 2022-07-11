


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self, root) -> None:
        self.root = root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        if key > root.val:
            root.right = self._insert(root.right, key)
        root.height = self.get_height(root)
        
        bf = self.get_balancefactor(root)

        # Single Left rotate (LL)
        if bf > 1 and key < root.left.val:
            return self.rightrotate(root)

        # Double rotate Left Right rotate (LR)
        if bf > 1 and key > root.right.val:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)

        # Single Right rotate (RR)
        if bf < -1 and key > root.right.val:
            return self.leftrotate(root)

        # Double rotate Left Right  rotate (LR)
        if bf < -1 and key < root.right.val:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)

        return root

    def largestleftnode(self, root):
        cur = root
        while cur.right:
            cur = cur.right
        return cur 

    def deleteNode(self, key):
        self.root = self._deletenode(self.root, key)

    def _deletenode(self, root, key):
        # standard BST delete
        if not root:
            return
        if key < root.val:
            root.left = self._deletenode(root.left, key)
        elif key > root.val:
            root.right = self._deletenode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                leftnode = self.largestleftnode(root.left)
                root.val = leftnode.val
                root.leftchild = self._deletenode(root.left, leftnode.val)

        if not root:
            return None
        
        root.height = self.get_height(root)
        
        bf = self.get_balancefactor(root)

        

        return root


    def leftrotate(self, node):
        cur_right_of_node = node.right
        left_of_cur_right = cur_right_of_node.left

        node.right = left_of_cur_right
        cur_right_of_node.left = node

        node.height = self.get_height(node)
        cur_right_of_node.height = self.get_height(cur_right_of_node)
        
        return cur_right_of_node

    def rightrotate(self, node):
        cur_left_of_node = node.left
        right_of_cur_right = cur_left_of_node.left

        node.left = right_of_cur_right
        cur_left_of_node.right = node

        node.height = self.get_height(node)
        cur_left_of_node.height = self.get_height(cur_left_of_node)
        return cur_left_of_node


    def get_balancefactor(self, root):
        return self.get_height(root.left) - self.get_height(root.right)

    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def get_bf(self, root):
        return 1 + max(root.left, root.right)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print (root.val)
        self.inorder(root.right)



root = TreeNode(1)

avl = AVLTree(root)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.insert(5)
avl.insert(6)

avl.inorder(avl.root)

avl.deleteNode(5)
print("after deletion")
avl.inorder(avl.root)

avl.insert(7)
avl.insert(8)
avl.insert(9)
print("=====")
avl.inorder(avl.root)