age = int(input("What is your age? "))

remaining_years = 90-age

days_in_a_year = 365
months_in_a_year = 12
weeks_in_a_year = 52

remaining_months = remaining_years*months_in_a_year
remaining_weeks = remaining_years*weeks_in_a_year
remaining_days = remaining_years*days_in_a_year

print(f"You have {remaining_days} Days, {remaining_weeks} Weeks, and {remaining_months} months left.")
