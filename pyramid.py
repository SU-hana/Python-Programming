""" DISPLAY THE GIVEN PYRAMID WITH STEP NUMBER ACCEPTED FROM USER. """

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
© 2022 GitHub, Inc.
Terms
