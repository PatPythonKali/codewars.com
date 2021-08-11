friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)
           ]
age = lambda x:x[1] >= 18
print(list(filter(age, friends)))