'''Write a function that returns a string in which firstname is swapped with last name.
name_shuffler('john McClane'); => "McClane john"'''

# Solution 1
def name_shuffler(str):
    str = str.split()
    str = (f"{str[1]} {str[0]}")
    return str

# Solution 2
def name_shuffler(str):
    return ' '.join(str_.split(' ')[::-1])

# Solution 3
def name_shuffler(str):
    str = str.split()
    print(" ".join(str[::-1]))

name_shuffler('john McClane')