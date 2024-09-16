class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 0:
            return True
        elif len(s) % 2 != 0:
            return False
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                openP = stack.pop()
                pair = openP + char
                print(pair)
                if pair != '()' and pair!='[]' and pair!='{}':
                    return False
        if len(stack) == 0:
            return True
        return False