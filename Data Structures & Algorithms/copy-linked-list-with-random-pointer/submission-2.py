class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        i = 0
        h = head
        res = Node(0)
        fres = res
        nodes_end = []

        while h:
            val = self.getNum(h.val, i)
            fres.val = val
            h.val = val
            nodes_end.append(fres)

            if h.next:
                fres.next = Node(0)

            fres = fres.next
            h = h.next
            i += 1

        h2 = res
        h3 = head
        while h2:
            if h3.random != None:
                _, idx = self.get_num_i(h3.random.val)
                h2.random = nodes_end[idx]
            else:
                h2.random = None

            og_num, _ = self.get_num_i(h2.val)
            h2.val = og_num

            h2 = h2.next
            h3 = h3.next

        return res

    def getNum(self, num, idx):
        idx_len = len(str(idx))

        sign = -1 if num < 0 else 1
        num = abs(num)

        return sign * (
            num * (10 ** (idx_len + 1))
            + idx * 10
            + idx_len
        )

    def get_num_i(self, num):
        sign = -1 if num < 0 else 1
        num = abs(num)

        idx_len = num % 10
        num //= 10

        idx = num % (10 ** idx_len)
        og_num = num // (10 ** idx_len)

        return og_num * sign, idx