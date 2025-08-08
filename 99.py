class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def swap_nodes(self,p1,isLeft,p2,isLeft2):
        if isLeft[0]:
            n1 = p1[0].left
        else:
            n1 = p1[0].right
        if isLeft2[0]:
            n2 = p2[0].left
        else:
            n2 = p2[0].right
        n1.val, n2.val = n2.val, n1.val

    def find_parents(self,root,p1,isLeft,p2,isLeft2):
        if root == None:
            return
        if root.left and root.left.val>root.val:
            if p1[0]==None:
                p1[0]=root
                isLeft[0]=True
            else:
                p2[0]=root
                isLeft2[0]=True
        if root.right and root.right.val<root.val:
            if p1[0]==None:
                p1[0]=root
                isLeft[0]=False
            else:
                p2[0]=root
                isLeft2[0]=False
        self.find_parents(root.left,p1,isLeft,p2,isLeft2)
        self.find_parents(root.right,p1,isLeft,p2,isLeft2)





    def recoverTree(self, root):
        p1 = [None]
        p2 = [None]
        isLeft = [False]
        isLeft2 = [False]
        self.find_parents(root,p1,isLeft,p2,isLeft2)
        self.swap_nodes(p1,isLeft,p2,isLeft2)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    solution.recoverTree(root)
    pass  # Replace with actual tree creation and testing code  