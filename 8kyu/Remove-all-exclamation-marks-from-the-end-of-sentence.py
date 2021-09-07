''' Remove all exclamation marks from the end of sentence. '''

def remove(s):
    return s.rstrip("!")

print( remove("Hi!!!") )