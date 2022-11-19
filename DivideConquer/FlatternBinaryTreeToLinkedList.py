class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class FlatternBinaryTreeToLinkedList:

    def flatten(self, root: TreeNode):
        return self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, root):
        if not root:
            return
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        return right_last or left_last or root

    prev = None
    def flatten1(self, root: TreeNode):
        if not root:
            return

        if self.prev is not None: # skip the first null prev node
            self.prev.right = root # we move curr node to the prev node's right
            self.prev.left = None # don't need to worry about losing original prev.right cuz we've already store it to "right"

        self.prev = root

        right = root.right # save root's right before flattening
        self.flatten(root.left)
        self.flatten(right)

    def print(self, root):
        while root:
            print(root.val)
            root = root.right


