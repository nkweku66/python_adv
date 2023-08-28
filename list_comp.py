#print positive numbers
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
post_numb = [x for x in numbers if x > 0]
print(post_numb)

#print even numbers
enumbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_numb = [x for x in enumbers if x % 2 == 0]
print(even_numb)

#print words and their len
words = ["hello", "my", "name", "is", "Sam"]
tup_list = [(word.upper(), len(word)) for word in words]
print(tup_list)