#Right-Angle Triangle (descending order)
rows = 7
for i in range(rows, 0, -1):  # Outer loop for rows
    for j in range(i):        # Inner loop for stars
        print('*', end='')
    print()                   # Move to the next line
