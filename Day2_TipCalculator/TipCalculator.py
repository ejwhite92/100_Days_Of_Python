print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input(
    'What percentage of the bill would you like to leave as a tip? 10, 15, or 20? '))
people = int(input('With how many people will you be splitting the bill? '))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = '{:.2f}'.format(bill_per_person)
print(f'Each person should pay: ${final_amount}')
