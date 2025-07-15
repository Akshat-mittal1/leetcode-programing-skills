class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        count = 0
        for i in nums:
            if i < 0:
                count += 1
        if count % 2 == 0:
            return 1
        return -1


if __name__ == "__main__":
    print(Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]))  # Output: 1
    print(Solution().arraySign([1, 5, 0, 2, -3]))           # Output: 0
