# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
        널도 값으로 가지고 있으니까
        결국 원소의 개수가중요하지 않을까?
        2로나눠지는 몫 + 1
        '''
        if root is None:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return level