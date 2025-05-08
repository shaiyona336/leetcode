class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # holds index of last unmatched ')'
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                # pop matching '(' or the sentinel
                stack.pop()
                if not stack:
                    # no boundary to match from, so set current ')' as boundary
                    stack.append(i)
                else:
                    # valid substring from stack.top()+1 to i
                    max_len = max(max_len, i - stack[-1])
        return max_len
    
solution = Solution()
s = "()"
result = solution.longestValidParentheses(s)
print(result)  # Expected output: 4 (the longest valid parentheses substring is "(()())")