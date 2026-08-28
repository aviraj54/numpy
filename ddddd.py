class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count=0
        d={}
        l=[]
        f=[]
        for i in range(len(s)):
            for j in range(len(s)-1):
                s1=s[i:j+1]
                l.append(s1)
            f.append(l)
        for k in range(len(f)):
            for x in (f[k]):
                for z in range(k+1,len(s)):
                    if x in f[z]:
                        count=count+1
                        d[x]=count
            count=0     
        for x1 in range (len(d)):
            for x2 in range (x1+1len(d)):
                if
