import calendar
year = int(input("Enter the year: "))
print(calendar.calendar(year, 3 ))
#3 is for the characters of the day, Mon
#to add others we can add 
'''print(calendar(year, 2, 1, 8, 4)) 
#2 = 2 characters for days (Mo,Tu, etc)
#1 = 1 line (row) for each week
#8 = 8 rows for each month
#4 = 4 columns for all months of the year.'''
