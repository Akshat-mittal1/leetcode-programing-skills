class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 0
        for j in digits:
            i = i * 10 + j
        i += 1
        l = len(str(i))
        digits = []
        for j in range(l):
            x = i // (10 ** (l - 1 - j))
            digits.append(x)
            i -= x * (10 ** (l - 1 - j))
        return digits

if __name__ == "__main__":
    # Test Case 1
    digits1 = [1, 2, 3]
    print(Solution().plusOne(digits1))  # Output: [1, 2, 4]

    # Test Case 2
    digits2 = [9, 9, 9]
    print(Solution().plusOne(digits2))  # Output: [1, 0, 0, 0]
