'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.'''

def lengthOfLastWord(self, s):
    s = s.split(' ')
    for i in s[:]:
        if i == ' ' or i == '':
            s.remove(i)
    return len(s[-1])