# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> Tuple[int, int]:
            if root is None:
                return (0, 0)
            L_rob, L_not = dfs(root.left)
            R_rob, R_not = dfs(root.right)
            rob_root = root.val + L_not + R_not
            not_rob_root = max(L_rob, L_not) + max(R_rob, R_not)
            return (rob_root, not_rob_root)
        return max(dfs(root))