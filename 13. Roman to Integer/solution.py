class Solution:
    def romanToInt(self, s: str) -> int:
        t = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        for i in range(0, n - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                t = t - roman[s[i]]
            else:
                t = t + roman[s[i]]
        t = t + roman[s[n - 1]]
        return t

