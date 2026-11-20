class Solution:
    def decodeString(self, s: str) -> str:        
        curr = 0
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        def parse_str():
            res_str = []
            nonlocal curr
            start_num = -1
            while curr < len(s):
                if s[curr] == '[':
                    print(start_num)
                    print(curr)
                    dup = int(s[start_num: curr])
                    curr +=1
                    res = parse_str()
                    for _ in range(dup): res_str.extend(res)
                    start_num = -1
                elif s[curr] in nums:
                    if start_num == -1:
                        start_num = curr
                elif s[curr] == ']':
                    return res_str
                else:
                    res_str.append(s[curr])
                curr += 1

            return res_str
        
        return ''.join(parse_str())