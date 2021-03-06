给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5


class Solution(object):
    def length_of_last_word(self, s):
        s = s.strip()
        if len(s) != 0:
            return len(s.split(" ")[-1])
        else:
            return 0


test = Solution()
result = test.length_of_last_word("hello world")
print(result)
