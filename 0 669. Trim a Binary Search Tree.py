669. Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/
  
#1. Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val <low:
            return self.trimBST(root.right,low,high)
        if root.val > high:
            return self.trimBST(root.left,low,high)
        else:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
        return root
      
#Time complexity: O(n)
#Space complexity:O(n)
