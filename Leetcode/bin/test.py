def lengthOfLongestSubstring(s: str) -> int:
    ans = 0
    lastLen = 0
    tempSet = set()
    start = 0
    i = 0
    while i < len(s):
        tempSet.add(s[i])
        if len(tempSet) <= lastLen:
            lastLen = 1
            start += 1
            i = start
            tempSet.clear()
            tempSet.add(s[start])
        else:  
            lastLen = len(tempSet)
            ans = max(lastLen,ans)
        i += 1
    return ans

print(lengthOfLongestSubstring('dvdf'))
