#QUESTION 2
print("****SAMPLE OUTPUT QUESTION 2****")

#part a
numListInches = [3.4*12,4.1*12,4*12,3.9*12,3.05*12,4.3*12,4.3*12,3.7*12]
avg = sum(numListInches)/len(numListInches)
formatedAvg = "{:.3f}".format(avg)
print("Average height in feet:",formatedAvg)

#partb
numListFeet = [3.4,4.1,4,3.9,3.05,4.3,4.3,3.7]

avg = sum(numListFeet)/len(numListFeet)
formatedAvg = "{:.1f}".format(avg)
print("Average height in feet:",formatedAvg)