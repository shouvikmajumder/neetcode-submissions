class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        /..//_home/a/b/..///
        '''

        operator_lst = path.split("/")
        stack = []
        for segment in operator_lst:
            if segment == "." or segment == "":
                continue
            elif segment == "..":
                if stack: 
                    stack.pop()
            else:
                stack.append(segment)

        return "/" + "/".join(stack)    