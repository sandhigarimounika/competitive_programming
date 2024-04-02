class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        count=0
        for i in range(len(s)):
            if i<=len(s)-k:
                j=s[i:i+k]
                l=int(j)
                if l!=0:
                    print(l)
                    if num%l==0:
                        count+=1
        return count




