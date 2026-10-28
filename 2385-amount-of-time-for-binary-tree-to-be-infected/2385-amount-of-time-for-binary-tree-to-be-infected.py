from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        """
        We need to get the max depth of both sides
        Once we hit infected node:
            we need to return its max depth from the poison

        root to poison
        poison to root 
        root to leaf
        """
        graph = defaultdict(list)

        def dfs(root):
            if not root:
                return
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        q = deque()
        
        q.append(start)
        visited = set([start])
        minute = -1

        while q:
            for _ in range(len(q)):
                popped = q.popleft()

                for n in graph[popped]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
            
            minute+=1
        
        return minute

        

                
            

