class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split(' ')
        s2 = ''
        i = 0
        while i < len(s1):
            if i == len(s1) - 1:
                s2 += s1[i][::-1]
            else:
                s2 = s2 + s1[i][::-1] + ' '
            i += 1
        return s2
