#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.23%)
# Total Accepted:    63.6K
# Total Submissions: 170.4K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 建立一个字典存储括号对，遍历字符串遇到左括号就压栈
        # 遇到右括号就寻找栈中前一个压入的元素是不是对应的左括号，是的话将其出栈，否则返回False
        # 遍历完成如果栈中还有元素则返回False，否则返回True
        dicts = {')':'(', '}':'{', ']':'['}
        stack = list()
        for item in list(s):
            if item in dicts.values():
                stack.append(item)
            else:
                if len(stack) != 0 and stack[-1] == dicts[item]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
        

