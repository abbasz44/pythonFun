
count = 0
sum = 0.0
number = 1

while number != -1:
    print "Please enter a mark between 0 and 100 or -1 to exit: "
    number = int(input(""))

    if number > 100:
	print("Invalid input!")

    else:
        sum = sum + number
        count += 1

    
    

    

print"Valid Test marks were entered", (count-1)
print"The average mark on the test is: ", sum/(count-1)