class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for item in s:
            if item in '({[':
                stack.append(item)
            else:
                if not stack or ( item == ')' and stack[-1] != '(' ) or ( item == '}' and stack[-1] != '{') or ( item == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack # if empty, it will be False. but 'not' makes True
                         # if not, it will be True. but 'not' makes False
