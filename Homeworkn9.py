word = "Sasha"
sim = "s"
word_new = ''
prew_x = 0
for x in word:
    if x not in word_new:
         prew_x += 1
         word_new = word_new + x

print(prew_x)
print(word_new)

