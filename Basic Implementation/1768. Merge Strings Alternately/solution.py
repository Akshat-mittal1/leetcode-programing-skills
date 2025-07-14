class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ret = ''
        l1 = len(word1)
        l2 = len(word2)
        en = min(l1, l2)

        for i in range(en):
            ret += word1[i] + word2[i]

        if l1 > l2:
            ret += word1[en:]
        elif l2 > l1:
            ret += word2[en:]

        return ret


if __name__ == "__main__":
    # Test Case 1
    print(Solution().mergeAlternately("abc", "pqr"))  # Output: "apbqcr"

    # Test Case 2
    print(Solution().mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
