class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == "__main__":
    # Test Case 1
    print(Solution().strStr("hello", "ll"))  # Output: 2

    # Test Case 2
    print(Solution().strStr("abc", "d"))     # Output: -1
