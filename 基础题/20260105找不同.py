#字符串t=字符串s+某一个额外字符+乱序，现在要找出多出来的那一个字符是什么
'''统计 s 中每个字母出现的次数
再统计 t 中每个字母出现的次数
找到那个 在 t 中次数更多的字母'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt={}#用字典来统计次数
        for ch in s:#遍历字符串s，cnt[ch]表示字符ch在s中出现了多少次
            if ch in cnt:
                cnt[ch]+=1
            else:
                cnt[ch]=1
        for ch in t:#遍历t，对字典做减法
            if ch in cnt:#如果ch在cnt中，说明ch在s中，说明不是新加的，抵消掉一个字符
                cnt[ch]-=1
                if cnt[ch]<0:#如果减完是负数，说明t中的字符比s多出来一个，是新加的，直接返回
                    return ch
            else:#如果ch不在cnt中，说明ch不在s中，说明ch是新加的字符，直接返回
                return ch
