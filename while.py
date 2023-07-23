#variable initialisations
total = 0
counter = 0

#this will loop until -1 is entered
while True:
    #asking the user to enter a number other than -1
    number = int(input("Enter a number other than -1: "))

    #if -1 is entered the code will stop
    if number == -1:
        break
    #add number to sum  and increment counter
    total+=number
    counter+=1

#if counter is not equal to 0, the average will be calculated
if counter !=0 :
    average = total / counter
    print("The Average of the Numbers Entered is equal to : ", average)
else:
    print("you Entered only -1!")