years = []
for year in range(1901,2000+1):
	years.append(year)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
daysInMonth = {
	'Sep' : 30,
	'Apr' : 30,
	'Jun' : 30,
	'Nov' : 30,
	'Jan' : 31,
	'Mar' : 31,
	'May' : 31,
	'Jul' : 31,
	'Aug' : 31,
	'Oct' : 31,
	'Dec' : 31,
	'Feb' : 28
}
daysInWeek = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
lengthOfWeek = len(daysInWeek)

def isLeapYear(year):
	if (year % 4) == 0 and ((year % 100) != 0 or (year % 400 == 0)):
		return True
	return False

firstSundays = 0
day = 2 # to start things off on a Monday
for year in years:
	for month in months:
		if daysInWeek[day % lengthOfWeek] == 'Sun':
			# print(month + ' ' + str(year))
			firstSundays += 1
		day += daysInMonth[month]
		if month == 'Feb' and isLeapYear(year):
			day += 1
print(firstSundays)