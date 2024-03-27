from os import path
from cryptography.fernet import Fernet, InvalidToken
# -------------------------------------------------------------------------------------------------

while True:
	key = input('Enter your Secret Key: ').encode('utf-8')

	try:
		f = Fernet(key)
	except Exception as e:
		print(e)
		print()
	else:
		print()
		break

while True:
	user_input = input('Is the Fernet Token in a file? (y/n)').lower()

	if user_input in ('yes', 'y'):
		file = input('Enter file path: ')

		try:
			with open(file, 'rb') as f1:
				token = f1.read()
		except FileNotFoundError as e:
			print(e)
			print()
			continue
		else:
			print()

	elif user_input in ('no', 'n'):
		token = input('Enter Fernet Token: ').encode('utf-8')
		print()

	else:
		print(f'"{user_input}" is not a valid input.\n')
		continue

	try:
		plaintext = f.decrypt(token).decode('utf-8')
	except InvalidToken:
		print(f'Token is not valid.\n')
	else:
		break

print(
	'Original plaintext:\n'
	f'{plaintext}'
)
print()
