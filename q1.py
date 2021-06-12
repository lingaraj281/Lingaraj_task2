print("Enter a sentence")
sentence = str(input())
num_of_letters = 0
for x in sentence:
    if(x != " "):
        num_of_letters = num_of_letters + 1 
num_of_words = 1
for y in sentence:
    if(y == " "):
        num_of_words =  num_of_words + 1
average_word_length = num_of_letters / num_of_words
print(average_word_length)
