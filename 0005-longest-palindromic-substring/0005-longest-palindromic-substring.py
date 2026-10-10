class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            length = max(odd, even)

            if length > end - start + 1:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]