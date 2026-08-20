class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for c in strs:
            encoded += c
            encoded += '~'

        return encoded


    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0

        while i < len(s):
            tmp = ""

            while s[i] != '~':
                tmp += s[i]
                i += 1
            
            decoded.append(tmp)
            i += 1

        return decoded
                    



