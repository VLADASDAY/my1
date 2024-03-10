# drop sequential duplicated symbols 

world = "coffeeeeeee" 
word_new = ''
prew_x = ''
for x in word:
    if x != prev_x:
         prev_x = x 
         word_new = word_new + x # word_new += x 

print(word)
print(word_new)
        
