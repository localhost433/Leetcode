# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def value(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            val = value(node.left) + value(node.right) + node.val
            freq[val] = freq.get(val, 0) + 1
            return val
        m = value(root)
        max_freq = max(freq.values())
        winners = [key for key, value in freq.items() if value == max_freq]
        return winners