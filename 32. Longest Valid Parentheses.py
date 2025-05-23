class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack != []:
                    best=max(best,i-stack[-1])
                else:
                    stack.append(i)

        return best