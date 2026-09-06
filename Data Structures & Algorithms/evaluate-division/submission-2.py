class Node:
    def __init__(self):
        self.adjNodes = {}
        self.adjNodeCalcs = {}

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        create a non directed graph
        with a source node, store values
        """

        # construct graph
        root = Node()
        for res, (var1, var2) in zip(values, equations):
            var1Node = root.adjNodes.setdefault(var1, Node())
            var2Node = root.adjNodes.setdefault(var2, Node())

            var1Node.adjNodes[var2] = var2Node
            var2Node.adjNodes[var1] = var1Node
            var1Node.adjNodeCalcs[var2] = res
            var2Node.adjNodeCalcs[var1] = 1 / res

        path = set()
        def dfs(curr: Node, target: Node, total):
            if curr == target:
                return total
                
            for var, nodeVar in curr.adjNodes.items():
                if var not in path:
                    path.add(var)
                    newTotal = total * curr.adjNodeCalcs[var]
                    res = dfs(nodeVar, target, newTotal)
                    path.remove(var)
                    if res != -1:
                        return res

            return -1

        qureyAnswer = []
        for var1, var2 in queries:
            var1Node = root.adjNodes.get(var1, None)
            var2Node = root.adjNodes.get(var2, None)
            if var1Node and var2Node:
                path.add(var1)
                qureyAnswer.append(dfs(var1Node, var2Node, 1.0))
                path.remove(var1)
            else:
                qureyAnswer.append(-1.0)

        return qureyAnswer


