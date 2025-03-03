'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
file = open("gardening_tips.txt", "r")
content = file.read()
splitcontent=content.split("\n")
for line in splitcontent:
    print(line)
file.close()




'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''


while True :
    hike = input("(input 0 to exit) Hike name:")
    if hike == "0":
        break

    distance = input ("How many miles?:")
    log = f"Hike Name: {hike}, Distance: {distance}\n"
    file=open("hikelog.txt", "a")
    file.write(log)


file = open("hikelog.txt", "r")
content = file.read()
print (content)


'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
wordcount={}
all_words=[]
count1=0
count2=0
count3=0
count4=0
count5=0
word1= str(input("Give me a first word you would like me to count:"))
word2= str(input("Give me a second word you would like me to count:"))
word3= str(input("Give me a third word you would like me to count:"))
word4= str(input("Give me a fourth word you would like me to count:"))
word5= str(input("Give me a fifth word you would like me to count:"))

with open("song_lyrics.txt", "r")as file:
    for line in file:
        stripped_line=line.strip()
        char_split=stripped_line.split()
        all_words.extend(char_split)

    for word in all_words:
        if word == word1:
            count1+=1
        elif word == word2:
            count2+=1
        elif word == word3:
            count3+=1
        elif word == word4:
            count4+=1
        elif word == word5:
            count5+=1
    wordcount[word1]=count1
    wordcount[word2]=count2
    wordcount[word3]=count3
    wordcount[word4]=count4
    wordcount[word5]=count5
    print(wordcount)




'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
with open("poll.txt", "r")as file:
    yea=0
    nay=0
    for line in file:
        stripped_line=line.strip()
        char_split=stripped_line.split(",")
    for word in char_split:
        if word == "yea":
            yea+=1
        elif word == "nay":
            nay+=1

    print("yea count:", yea,"nay count:", nay)



