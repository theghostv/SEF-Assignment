Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

letter=input("Search by letters:")
length_of_names = len(Names)
count = 0
for word in Names: 
    if letter.lower() in word.lower():
        print(word)
    else:
        count += 1
if count == length_of_names:
    print("Letter not found in any of the names")