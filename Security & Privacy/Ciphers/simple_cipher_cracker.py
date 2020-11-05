try:
	from langdetect import detect
except ImportError:
	print('Please pip install langdetect')

SMALL_ALPHABEIT = 'abcdefghijklmnopqrstuvwxyz'
CAPITAL_ALPHABEIT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SPECIAL = '~!@#$%^&*()_=-+`/.,\\<>?:"{}|[];\' '

ANSWERS = {
	0: SMALL_ALPHABEIT,
	1: CAPITAL_ALPHABEIT,
	2: NUMBERS,
}


def decipher(sentence: str, key: int, ignore: str):
	"""
	Deciphers the given sentence.
	:param sentence: the sentence to decipher.
	:param key: The key to use in the deciphering.
	:param ignore: A string of characters to ignore.
	:return: the deciphered sentence.
	:rtype: str
	"""
	new_sentance = ''

	for char in sentence:
		if char.isdigit():  # if its a digit
			if char not in ignore:
				new_sentance += chr((ord(char) - key - ord('0')) % len(NUMBERS) + ord('0'))
			else:
				new_sentance += char
		elif char.isupper():  # if its a capital letter
			if char not in ignore:
				new_sentance += chr((ord(char) - key - ord('A')) % len(CAPITAL_ALPHABEIT) + ord('A'))
			else:
				new_sentance += char
		elif char.islower():  # if its a small letter
			if char not in ignore:
				new_sentance += chr((ord(char) - key - ord('a')) % len(SMALL_ALPHABEIT) + ord('a'))
			else:
				new_sentance += char
		else:  # if its a symbol
			new_sentance += char

	return new_sentance


def main():
    """
    Main function.

    Args:
    """
	sentences = {}
	ignores = ''

	ciphered_sentance = input('Enter the ciphered sentence: ')

	answer = 0
	while answer is not 4:
		try:
			print(
				f'''
Enter the numbers you want to ignore in the deciphering process:
0. Ignore small letters. {SMALL_ALPHABEIT}
1. Ignore capital letters. {CAPITAL_ALPHABEIT}
2. Ignore numbers. {NUMBERS}
3. Custom symbols.
Currently ignoring: {''.join(set(ignores))}

Press Return to continue.
'''
			)
			answer = input('Enter your choice: ')
			if answer is '':  # Check if its the exit sign(Nothing)
				print('Deciphering...')
				break
			ignores += ANSWERS[int(answer)]
		except ValueError:  # If its not an integer
			print('Invalid choice.')
		except KeyError as e:  # If its not form the ANSWERS dictionary
			if e.args[0] == 3:  # Check if its a custom ignore
				custom_ignore = input('Enter the symbols to ignore: ')
				ignores += custom_ignore
			else:
				print('Invalid choice.')

	ignore = ''.join(set([SPECIAL, ignores]))

	#  Get all the possible combinations
	for key in range(1, 26):
		sentences[key] = decipher(ciphered_sentance, key, ignore)

	#  Check if it thinks its English or not, print if it thinks
	found = 0
	for key in sentences.keys():
		try:
			if detect(sentences[key]) == 'en':  # Check to see if it thinks its English
				found += 1
				print(f'Maybe {key} is a possibility because I got: "{sentences[key]}"')
		except Exception:
			pass

	#  Tell the user if it didn't find anything
	if found == 0:
		print('I didn\'t find anything...')

	print('Do you want to see every possibility? [y/n]')
	answer = input('')
	if answer == 'y':
		for key in sentences.keys():
			print(f'{key}: {sentences[key]}')


if __name__ == "__main__":
	main()
