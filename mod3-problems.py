# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated.Use the skills you learned in this module to print the word the correct number of times.
word=(input("Give me a word:"))
word_repeated=int(input("How many times would you like that word repeated:"))
print(word * word_repeated)

#2. Prompt the user for their name and their age. Calculate their age next year.
#Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name=input("What is your name?")
age1=(int(input("What is your age?")))
age2= (age1+1)
print("Hello "+ name +"! you are "+str(age1)+" years old. Next year, you will be "+str(age2)+" years old.")


#3. Prompt the user for a sentence and a word to try to find in that sentence.
#Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence=input("What is your sentence?")
word=input("What is your word?")
print(word in sentence)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word=input("What is your word")
index1=int(input("What is your first index"))
index2=int(input("What is your last index"))
print(word[index1:index2])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
phrase="big german shepard"
phrase2=(phrase.split(" "))
print(("|").join(phrase2))
