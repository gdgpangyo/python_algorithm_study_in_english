# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.dfs(p) == self.dfs(q)
        #return self.bfs(p) == self.bfs(q)
    
    def dfs(self, node):
        if node != None:
            return [node.val] + self.dfs(node.left) + self.dfs(node.right)
        
        return ["None"] # mark dangling child for comparison
    
    def bfs(self, root):
        if root == None:
            return []
        return [root.val] + self.bfsNode(root)    
        
    def bfsNode(self, node):
        result = []
        if node != None: # mark dangling child for comparison
            result.append(node.left.val) if node.left != None else result.append("None")
            result.append(node.right.val) if node.right != None else result.append("None")
            return result + self.bfsNode(node.left) + self.bfsNode(node.right)
        
        return []    
            
        
