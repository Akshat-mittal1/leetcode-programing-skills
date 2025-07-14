class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        a = sorted(s)
        b = sorted(t)
        if a != b:
            return False
        return True

if __name__ == "__main__":
    # Test Case 1
    print(Solution().isAnagram("anagram", "nagaram"))  # Output: True

    # Test Case 2
    print(Solution().isAnagram("rat", "car"))          # Output: False
