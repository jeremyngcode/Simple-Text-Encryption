from os import path
from cryptography.fernet import Fernet
# -------------------------------------------------------------------------------------------------

while True:
	user_input = input('Do you need a fresh Fernet Secret Key? (y/n)').lower()

	if user_input in ('yes', 'y'):
		print('Generating fresh secret key..\n')
		key = Fernet.generate_key()

		print(
			'Your new Secret Key:\n'
			f'{key.decode("utf-8")}\n')
		break

	elif user_input in ('no', 'n'):
		print()
		break

	else:
		print(f'"{user_input}" is not a valid input.\n')

msg = input('Enter the text you want to encrypt: ').encode('utf-8')
print()

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

filename = input('Enter filename: ')
file_path = path.join(path.dirname(__file__), filename)
print()

token = f.encrypt(msg)

with open(filename, 'wb') as new_file:
	new_file.write(token)

print(f'Encryption complete, Fernet Token saved to "{file_path}"')
print()
