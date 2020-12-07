#кількість входжень слів (better, never, is)
str_python = "Now is better than never"
split_words = str_python.split()
print ("split_words", split_words)

count1 = split_words.count('better')
count2 = split_words.count('never')
count3 = split_words.count('is')

print ("The count better is", count1)
print ("The count never is", count2)
print ("The count is", count3)

#Вивести весь текст у верхньому регістрі (всі великі літери)
print (str_python.upper())

# Замінити всі входження символу “і” на “&”
print (str_python.replace ('i', '&'))