class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathParts = path.split('/')
        for part in pathParts:
            if part == '' or part == '.':
                continue

            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)