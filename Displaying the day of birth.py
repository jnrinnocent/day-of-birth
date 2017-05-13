      #   WEREDWONG INNOCENT
      #REG No.:16/U/1278
      #Displaying the day of birth

#importing the datetime, and calendar module
import datetime,calendar
#Setting the current date according to the computer's date
cur_year = int(datetime.date.today().strftime('%Y'))

date = input("Enter birth date (1-31)\n")

endings = ["st", "nd", "rd"]+ 17*["th"] + ["st", "nd", "rd"] + 7*["th"] + ["st"]

days = ['Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday',
        'Sunday']

month = int(input("Enter the month in which you were born in(1-12)\n"))

month_names = ['January','February','March',
                'April','May','June',
                'July','August','September',
                'October','November','December']

age = int(input("How old are you now? \n"))

var1 = month_names[month-1]
var2 = int(date)
var3 = (cur_year-age)
var4 = date+endings[var2-1]
var5 = calendar.weekday(var3,month,var2)
var6 = days[var5]
#printing the date and year
print("You were born on",var6 ,var4, var1,", " ,var3)
