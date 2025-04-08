print("Введите пароль: ", end = '')
password = input()
score = 0

def is_very_long(password):
	if len(password) > 12:
		return True
	else:
		return False

def has_digits(password):
	for letter in password:
		if letter.isdigit() == True:
			found_digit = True
			return found_digit
		else:
			found_digit = False
	return found_digit

def has_upper_letters(password):
	for letter in password:
		if letter.isupper() == True:
			found_upletter = True
			return found_upletter
		else:
			found_upletter = False
	return found_upletter

def has_lower_letters(password):
	for letter in password:
		if letter.islower() == True:
			found_lowletter = True
			return found_lowletter
		else:
			found_lowletter = False
	return found_lowletter

def has_symbol(password):
	for letter in password:
		if letter.isdigit() == False and letter.isalpha() == False:
			found_symbol = True
			return found_symbol
		else:
			found_symbol = False
	return found_symbol

password_score = [is_very_long(password),has_digits(password),has_upper_letters(password),has_lower_letters(password), has_symbol(password)]
for check in password_score:
	if check == True:
		score += 2

print("Рейтинг пароля:", score)