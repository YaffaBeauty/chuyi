#!/usr/bin/env python
# -*- coding:utf-8 -*-
leet_a = "abcabcbb"
leet_b = "bbbbbb"

"""从第一个字符串开始依次遍历字符串,不同的字符做累加，顺序取出不重复的子串，存到字典中，key为子串s，value为len(s),当遇到重复的字符时，就新起一个子串
如在字符串leet_a中顺序取出abc,当第四个字符为a,在前面的子串abc中，就另起一个子串bca,当第五个字符为b,在前面字符bca中，就另起一个子串cab....
字典s_dict={'abc':3,'bca':3,'cab':3,'abc':3,'bc':2,'cb':2,'b':1},取最大value即为最大子串长度
"""


class Solution():
    def lengthOfLongestSubstring(self, s):
        s_dict = {}
        for i in range(len(s)):
            max_s = s[i]
            j = i
            while j < len(s):

                if j < len(s)-2 and s[j+1] not in max_s:
                    max_s = max_s + s[j+1]
                    j = j + 1
                else:
                    break
            s_dict[max_s] = len(max_s)

        result_list = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)

        return result_list[0][1]


if __name__ == '__main__':

    sol = Solution()
    print(sol.lengthOfLongestSubstring(leet_a))






