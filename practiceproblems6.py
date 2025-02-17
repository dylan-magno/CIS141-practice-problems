# Write your code here :-)
#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(sum(b))



#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
stringlist=["Olympic", "Students", "Rangers", "School", "Olympic"]
count=0
for string in stringlist:
    if "Olympic" in string:
       count += 1
print(count)

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters.
#Print the resulting filtered list.
strings=["Cat", "Water", "Bug", "Happy"]
filteredlist=[]

for string in strings:
    if len(string) > 3:
        filteredlist.append(string)
print(filteredlist)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
integers = [ 1, -4, 3, 9, -10]
pos = 0
neg = 0
for integer in integers:
    if integer > 0:
        pos += 1
    else: neg += 1
print("Positive numbers:", pos, "\nNegative numbers:", neg)

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list.
#Print the new list.
integerlist=[2,4,6,8,10]
squarelist=[]

for integer in integerlist:
    squared=integer*integer
    squarelist.append(squared)
print(squarelist)



