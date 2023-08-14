def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leapYear = True
            else:
                leapYear = False
        else:
            leapYear = False
    else:
        leapYear = False

    return leapYear

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    leapCheck = is_leap(year)
    if (leapCheck) and month == 2:
        return 29 
    return month_days[month-1]







year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year,month)
print(days)