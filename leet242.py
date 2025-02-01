s="anagram"
t="nagaram"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for j in t:
    if j not in d:
        return False
    else:
        if f[j]==1:
            del d[j]
        elif d[j]>1:
            d[j]-=1
if d=={}:
    return True
else:
    return False