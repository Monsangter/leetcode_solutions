# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
        널도 값으로 가지고 있으니까
        결국 원소의 개수가중요하지 않을까?
        2로나눠지는 몫 + 1
        '''
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1
        print(root)
        print(root.right)
        # return len(root) // 2 + 1