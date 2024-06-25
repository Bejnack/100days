bleap_year = True

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year")
        bleap_year = True
        return bleap_year
      else:
        #print("Not leap year")
        bleap_year = False
        return bleap_year
    else:
      #print("Leap year")
      bleap_year = True
      return bleap_year
  else:
    #print("Not leap year")
    bleap_year = False
    return bleap_year
  
# TODO: Add more code here 👇
def days_in_month(year ,month):
    b_leap_year = is_leap(year)
    print(b_leap_year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if b_leap_year == False:
        month_days[1] = 29
    return month_days[month - 1]
#29 on non leap year
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

