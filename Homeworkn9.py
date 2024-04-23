word = "Sasha"
sim = "s"
word_new = ''
count = 0

for i in word.lower():
     if sim != i:
        count += 1 
print(count)