#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []
        for letter in s:
            match letter:
                case "(" | "[" | "{":
                    tracker.append(letter)
                case ")":
                    if tracker and tracker[-1] == "(":
                        tracker.pop()
                    else:
                        return False
                case "]":
                    if tracker and tracker[-1] == "[":
                        tracker.pop()
                    else:
                        return False
                case "}":
                    if tracker and tracker[-1] == "{":
                        tracker.pop()
                    else:
                        return False
        if tracker: return False
        return True
# @lc code=end
