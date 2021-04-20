#QUESTION 1
print("****SAMPLE OUTPUT QUESTION 1****")

#part a
#declaring varibales for calculation
travel = 50
gallons= 15
#calculate gallons of fuel
ans = travel/gallons 

#print first sample output
print("Gallons of Fuel to travel 50 miles:", ans)

#part b
#24 km per gallon 

travel1 = 50
gallon1 = 24

#calculate
ans2 =  travel1/gallon1
#two decimal points
formatAns = "{:.2f}".format(ans)

print("Gallons of fuel to travel 50 km:", formatAns)

#part c

gallon2 = 24 
tank = 17.5 
#calculate
distance = gallon2*tank

#format
formatDistance = int(distance)

print("Distance travelled on full tank: ", formatDistance, "km")




