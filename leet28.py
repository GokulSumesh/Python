# haystack = "sadbutsad"
# needle = "sad"
# for i in range(len(haystack)):
#     if haystack[i]=="sad":
#         print(0)
#         break
#     else:
#         print(-1)
#         break


haystack = "sadbutsad"
needle = "sad"
a = haystack.find(needle)
if a != -1:
    print(a)  
else:
    print(-1)