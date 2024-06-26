# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)

        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


if __name__ == '__main__':
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.left.left = TreeNode(val=7)
    root.left.right = TreeNode(val=6)
    root.right.left = TreeNode(val=5)
    root.right.right = TreeNode(val=4)
    sol = Solution()
    result = sol.maxDepth(root)
    print(result)
