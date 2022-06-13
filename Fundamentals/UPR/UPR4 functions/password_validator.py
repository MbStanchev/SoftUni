password = input()

def password_lenth_validator(word):
    result = None
    if 6  <= len(word) <= 10:
        return True
    else:
        print("Password must be between 6 and 10 characters")
        return  False

def pass_is_all_num_sim(word):
    if word.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")
        return False

def two_digits(word):
    dig_couter = 0
    for char in word:
        if char.isdigit():
            dig_couter += 1
    if dig_couter >= 2:
        return True
    else:
        print("Password must have at least 2 digits")
        return False

# if password_lenth_validator(password) and two_digits(password) and pass_is_all_num_sim(password):
valid = [password_lenth_validator(password), pass_is_all_num_sim(password), two_digits(password)]
if all(valid):
    print("Password is valid")
