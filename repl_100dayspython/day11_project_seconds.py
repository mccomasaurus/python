##Math Variables##
seconds_1_minute = 60
minutes_1_hour = 60
hours_1_day = 24
days_1_year = 365
days_leap_year = 366

print("#####################")
print("We are going to calulcate how many seconds are in a year")
print()
leap = input("Is this a leap year?: ")
if leap == "yes":
  answer = (seconds_1_minute * minutes_1_hour * hours_1_day * days_leap_year)
  print("days in a year is,", answer)
else:
  answer = (seconds_1_minute * minutes_1_hour * hours_1_day * days_1_year)  
  print("days in a year is,", answer)
