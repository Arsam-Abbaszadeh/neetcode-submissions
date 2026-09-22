class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        treat n / as 1
        .. removes path before unles already at root
        """
        # stack = []
        # pathParts = path.split('/')
        # for part in pathParts:
        #     if part == '' or part == '.':
        #         continue

        #     if part == '..':
        #         if stack:
        #             stack.pop()
        #     else:
        #         stack.append(part)

        # return '/' + '/'.join(stack)


        strParts = deque()
        pathParts = path.split('/')
        skipFolder = 0
        for i in range(len(pathParts) - 1, -1, -1):
            part = pathParts[i]
            if part == '' or part == '.':
                continue

            if part == '..':
                skipFolder += 1

            elif skipFolder:
                skipFolder -= 1
            else:
                strParts.appendleft(part)

        return '/' + '/'.join(strParts)
