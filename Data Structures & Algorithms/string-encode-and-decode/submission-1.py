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
        skip = 0
        for i, char in enumerate(s):
            if skip > 0:
                skip -= 1
            else:
                delim = i
                while s[delim] != "$":
                    delim += 1

                word_len = int(s[i: delim])
                skip = word_len + delim - i

                decoded.append(s[delim + 1: delim + word_len + 1])

        return decoded
