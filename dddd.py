from functools import reduce

def joined_words(s1,s2):
    return s1 + " " + s2

words = 'mr', "gh" ,'god'
combined = reduce(joined_words, words)
print(combined)
