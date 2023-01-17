#Напишите программу, удаляющую из текста все слова, содержащие "абв". 
#В тексте используется разделитель пробел.

from random import sample
text = "абв"

num_word = (int(input("Количество слов: ")))
list_word = []

for x in range(num_word):
    random_text = sample(text, 3)
    list_word.append("".join(random_text))
print(" ".join(list_word))

list_word2 = list(filter(lambda x: text not in x, list_word))
print(" ".join(list_word2))
