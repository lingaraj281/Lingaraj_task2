print("Enter a text")
a=str(input())
letter = input("Enter a letter\n")
letter_count = 0
for x in a:
    if x == letter:
        letter_count = letter_count + 1
num_of_letters = 0
for x in a:
    if(x != " "):
        num_of_letters = num_of_letters + 1 
frequency = (letter_count/num_of_letters)*100
print(frequency)