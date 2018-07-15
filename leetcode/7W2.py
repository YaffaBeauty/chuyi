#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""将数组分成两部分，两部分中的和相等"""


class Solution():
    def canPartition(self, nums):
        if nums == []:
            return True
        if sum(nums) % 2 == 1:
            return False
        half_sum = int(sum(nums) / 2)

        res = []
        for i in range(half_sum + 1):
            res.append(False)
        res[0] = True
        for i in nums:
            j = half_sum
            while j >= i:
                res[j] = res[j] or res[j - i]
                j = j - 1
        return res[half_sum]


if __name__ == '__main__':
    a = [5, 10, 4, 25, 23, 21]
    b = [1, 2, 3, 5]
    c = [1, 5, 11, 5]
    print(Solution().canPartition(c))
