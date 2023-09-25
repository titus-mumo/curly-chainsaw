'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''


def strStr(self, haystack, needle):
    index = None
    status = False
    last_consideration = len(haystack) - len(needle)
    for i in haystack[:last_consideration+1]:
        index_i = haystack.index(i)
        end_index = index_i + len(needle)
        word = haystack[index_i: end_index]
        if word == needle:
            status = True
            index = index_i
            continue
    if status == True:
        return index
    else:
        return -1