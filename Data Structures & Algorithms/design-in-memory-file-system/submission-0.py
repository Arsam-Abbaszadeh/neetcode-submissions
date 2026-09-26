from collections import defaultdict
from typing import List, final

class Directory:
    def __init__(self):
        self.subDirectories = defaultdict(Directory)
        self.files = defaultdict(str)

class FileSystem:
    def __init__(self):
        self.root = Directory()

    def ls(self, path: str) -> List[str]:
        parts = self.getFileParts(path)
        currDir = self.root
        for i in range(len(parts) - 1):
            # assuming no non existent file pxqaths
            currDir = currDir.subDirectories[parts[i]]

        if not parts or parts[-1] in currDir.subDirectories:
            finalDir = currDir
            if parts:
                finalDir = currDir.subDirectories[parts[-1]]
            res = list(finalDir.subDirectories.keys())
            res += list(finalDir.files.keys())
            res.sort()
            return res
        return [parts[-1]]

    def mkdir(self, path: str) -> None:
        parts = self.getFileParts(path)
        currDir = self.root
        for i in range(len(parts)):
            currDir = currDir.subDirectories[parts[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = self.getFileParts(filePath)
        currDir = self.root
        for i in range(len(parts) - 1):
            currDir = currDir.subDirectories[parts[i]]

        currDir.files[parts[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        parts = self.getFileParts(filePath)
        currDir = self.root
        for i in range(len(parts) - 1):
            currDir = currDir.subDirectories[parts[i]]

        return currDir.files.get(parts[-1], '')

    def getFileParts(self, path):
        if path == '/':
            return []
        return path.split('/')[1:]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
# filesys.mkdir('/a/b/c')
# filesys.addContentToFile('/a/b/c/d', 'hello')
# print(filesys.ls('/'))
# filesys.readContentFromFile("/a/b/c/d")