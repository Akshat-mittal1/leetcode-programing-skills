class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = m = len(s)
        l = l // 2
        while l > 0:
            if m % l == 0:
                res = ''
                x = s[:l]
                y = m // l
                for i in range(y):
                    res += x
                if res == s:
                    return True
            l -= 1
        return False

if __name__ == "__main__":
    # Test Case 1
    print(Solution().repeatedSubstringPattern("abab"))  # Output: True

    # Test Case 2
    print(Solution().repeatedSubstringPattern("aba"))   # Output: False
