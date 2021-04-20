flag = False

print "Please enter a mark between 100 and 200" 
number = int(input(""))

if number >= 100 or number <= 200:
    for i in range(2, number):
        if (number % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
       # else: 
    #    print("You entered outside the valid range")
if flag:
    print number, "is NOT a prime number"
else:
    print number, "is a prime number"