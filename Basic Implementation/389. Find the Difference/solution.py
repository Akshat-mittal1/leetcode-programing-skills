class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for i in s:
            res ^= ord(i)
        for i in t:
            res ^= ord(i)
        return chr(res)


if __name__ == "__main__":
    # Test Case 1
    print(Solution().findTheDifference("abcd", "abcde"))  # Output: "e"

    # Test Case 2
    print(Solution().findTheDifference("", "y"))  # Output: "y"
