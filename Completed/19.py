# 1-indexing
def month_length(month, year):
  # 30 days in April(4), June(6), September(9) and November(11)
  months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

  if month == 2 and year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return months[month] + 1
      else:
        return months[month]
    else:
      return months[month] + 1
  else:
    return months[month]

# Day zero is 1. Jan 1900 and was monday
# Day is also zero indexed. If day % 7 == 0 then sunday
day = 0
sundays = 0

for y in range(1900,2001):
  print "Year: " + str(y)
  for m in range(1,13):
    print "Month: " + str(m)
    day += month_length(m,y)
    print day
    if y > 1900:
      if y == 2000 and m == 12:
        break;
      if day % 7 == 6:
        sundays += 1
    print sundays

print sundays
