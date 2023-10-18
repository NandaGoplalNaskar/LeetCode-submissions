class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        left_and_right_child = set(leftChild + rightChild)
        left_and_right_child.discard(-1)

        if len(left_and_right_child) == n:
            return False

        visited = set()
        #set the root node

        for i in range(n):
            if i not in left_and_right_child:
                root = i

        def dfs(node):
            if node == -1:
                return True

            if node in visited:
                return False
            visited.add(node)

            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(root) and len(visited) == n



        