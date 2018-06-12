'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend = ['Saturday','Sunday']


def sleeping(b_day, b_vacation):
	print(f"Weekday: {b_day}, Vacation: {b_vacation}")
	if b_vacation == True:
		print("True : We are sleeping")
	elif b_vacation == False and b_day == False:
		print("True : We are sleeping")
	else:
		print("False : We are not sleeping")
	


if __name__ == "__main__":
	
	b_day = ''
	b_vacation = ''

	v_vacation = input("Are you on Vacation? (Yes/No) ::")
	if v_vacation in ['Yes','YES','yes','Y','y']:
		b_vacation = True
	elif v_vacation in ['No','NO','no','N','n']:
		b_vacation = False
	else:
		print("Wrong Input")

	v_day = int(input("Today is? \nMonday:- 1\nTuesday:-2\nWednesday:-3\nThursday:-4\nFriday:-5\nSaturday:-6\nSunday:-7 ::\n"))
	if v_day in range(0,6):
		b_day = True
	elif v_day in [6,7]:
		b_day = False
	else:
		print("Wrong Input")

	if b_day != '' and b_vacation != '':
		sleeping(b_day,b_vacation)
	else:
		print("Try again")