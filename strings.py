def strStr(haystack, needle):
    arr = []
    index = None
    status = False
    last_consideration = len(haystack) - len(needle)
    for i in haystack[:last_consideration+1]:
        index_i = haystack.index(i)
        end_index = index_i + len(needle)
        word = haystack[index_i: end_index]
        arr.append(word)
        if word == needle:
            status = True
            index = index_i
            continue
    if status == True:
        return index
    else:
        return arr

print(strStr('mississippi', 'issip'))