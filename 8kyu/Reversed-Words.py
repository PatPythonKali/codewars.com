''' Complete the solution so that it reverses all of the words within the string passed in. '''
str= 'The greatest victory is that which requires no battle'
def reverse_words(s):
    s = s.split()
    s = s.reverse()
    return s

print(reverse_words(str))