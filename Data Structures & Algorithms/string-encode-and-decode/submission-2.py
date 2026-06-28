class Solution:
    def encode(self, strs: List[str]) -> str:
        final = []
        for str in strs:
            final.append(f'{len(str)}')
            final.append("$")
            final.append(str)

        return ''.join(final)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j +=1
            word_len = int(s[i:j])
            decoded.append(s[j + 1: word_len + 1 + j ])
            i = j + 1 + word_len
        return decoded
