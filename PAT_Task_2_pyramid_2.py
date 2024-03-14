rows = 6  # the number of rows in the pyramid.
count = 1# initial value of 1 its printed in pyramid 

for i in range(1, rows + 1):#Outer loop iterating over each row of the pyramid.
    for j in range(1, rows - i + 1):#Inner loop printing spaces before each row for alignment.
        print(" ", end="")
    for k in range(1, i + 1):#Inner loop printing the numbers in each row.
        print(count, end=" ")#Prints the current count followed by a space.
        count += 1#Increments the count for the next number.
        if count > 20:# if the count exceeds 20, breaking out of loops if true.
            break
    print()
    if count > 20:# if count exceeds 20, breaking the outer loop if true.
     break
