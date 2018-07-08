#!/usr/bin/env python
# -*- coding:utf-8 -*-
leet_a = "abcabcbb"
leet_b = "bbbbbb"

"""从第一个字符串开始依次遍历字符串,不同的字符做累加，顺序取出不重复的子串，存到字典中，key为子串s，value为len(s),当遇到重复的字符时，就新起一个子串
如在字符串leet_a中顺序取出abc,当第四个字符为a,在前面的子串abc中，就另起一个子串bca,当第五个字符为b,在前面字符bca中，就另起一个子串cab....
字典s_dict={'abc':3,'bca':3,'cab':3,'abc':3,'bc':2,'cb':2,'b':1},取最大value即为最大子串长度
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        s_dict = {}
        for i in range(len(s)):
            max_s = s[i]
            # todo 条件实现，如何把条件连起来，想着用递归调用(考虑栈溢出和实现过程)
            if i < len(s)-2 and s[i+1] not in max_s:
                max_s = max_s+s[i+1]
            if i + 1 < len(s)-2 and s[i+1+1] not in max_s:
                max_s = max_s+s[i+1+1]

            s_dict[s] = len(max_s)
        result_list = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)

        return result_list[0][1]





