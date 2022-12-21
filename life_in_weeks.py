age = input('What is your current age? ')

years_left = 90 - float(age)
months_left = int(years_left * 12)
weeks_left = int(years_left * 52)
days_left = int(years_left * 365)
message = f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.'

print(message)