numbers = [-12, 4, 12, 25, 67]

repeat = True
while repeat == True:

    number=int(input("Insert number here:"))
    numbers.append(number)
    list_sorted=sorted(numbers)

    print(list_sorted)

    if number == -99:
        repeat = False
