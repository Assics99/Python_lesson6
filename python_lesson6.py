def is_very_long(password):
	return len(password) > 12
def has_digits(password):
	return any(character.isdigit() for character in password)
def has_upper_letters(password):
	return any(character.isupper() for character in password)
def has_lower_letters(password):
	return any(character.islower() for character in password)
def has_symbol(password):
	return any(not character.isdigit() and not character.isalpha() for character in password)

def main(): 
	print("Введите пароль: ", end = '')
	password = input()
	score = 0
	password_score = [
		is_very_long(password),
		has_digits(password),
		has_upper_letters(password),
		has_lower_letters(password), 
		has_symbol(password),
	]
	for check in password_score:
		if check:
			score += 2
	print("Рейтинг пароля:", score)

if __name__ == '__main__':
    main()
