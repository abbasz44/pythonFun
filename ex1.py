
marklist = [['John', 86.5], ['Joe', 42], ['Mary', 95], ['Tim', 70.2],['Jill', 65.8]]


for i in marklist:
    ##print(i[1])

    if i[1] < 50: 
        mark = 'F'
    if i[1] >= 50 and i[1] < 60:
        mark = 'D'
    if i[1] >= 60 and i[1] < 70:
        mark = 'C' 
    if i[1] >= 70 and i[1] < 80:
        mark = 'B'
    if i[1] >= 80 and i[1] <= 100:
        mark = 'A'
    
    print "NAME:", i[0], "MARK:", i[1], "GRADE:", mark