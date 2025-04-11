print("Введите пароль: ", end = '')
PASSWORD = input()

def is_very_long(password):
	return len(PASSWORD) > 12

def has_digits(password):
	return any(character.isdigit() for character in PASSWORD)

def has_upper_letters(password):
	return any(character.isupper() for character in PASSWORD)

def has_lower_letters(password):
	return any(character.islower() for character in PASSWORD)

def has_symbol(password):
	return any(not character.isdigit() and not character.isalpha() for character in PASSWORD)

def do_things():
	score = 0
	password_score = [
		is_very_long(PASSWORD),
		has_digits(PASSWORD),
		has_upper_letters(PASSWORD),
		has_lower_letters(PASSWORD), 
		has_symbol(PASSWORD)
	]

	for check in password_score:
		if check:
			score += 2

	print("Рейтинг пароля:", score)

def main(): 
    do_things()

if __name__ == '__main__':
    main()
