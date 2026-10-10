class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        center = right = 0
        best_center = best_len = 0

        for i in range(n):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while (
                i - p[i] - 1 >= 0
                and i + p[i] + 1 < n
                and t[i - p[i] - 1] == t[i + p[i] + 1]
            ):
                p[i] += 1

            if i + p[i] > right:
                center, right = i, i + p[i]

            if p[i] > best_len:
                best_center, best_len = i, p[i]

        start = (best_center - best_len) // 2
        return s[start : start + best_len]
