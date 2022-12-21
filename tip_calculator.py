print('Welcome to the tip calculator.')

bill = float(input('What was the total bill? $'))
bill_tip_percentage = float(input('What percentage tip would you like to give? '))
people_splitting_bill = int(input('How many people to split the bill? '))

bill_with_tip = bill * (1 + (bill_tip_percentage / 100))
bill_per_person = '{0:.2f}'.format(bill_with_tip / people_splitting_bill)
message = f'Each person should pay: ${bill_per_person}'

print(message)