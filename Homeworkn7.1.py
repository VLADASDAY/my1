# drop sequential duplicated symbols 

word = "suuuuuuuuun" 
word_new = ''
prew_x = ''
for x in word:
    if x != prew_x:
         prew_x = x 
         word_new = word_new + x # word_new += x 

print(word)
print(word_new)
        
