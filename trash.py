x = 'hello world'

def reverse_words(str):
    return " ".join(str.split(" ")[::-1])


print(reverse_words(x))