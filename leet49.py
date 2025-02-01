strs = ["eat","tea","tan","ate","nat","bat"]
for i in strs:
    s="".join(sorted(i))
    if s not in d:
        d[s]=[i]
    else:
        d[s].append(i)
print(list(d.values()))