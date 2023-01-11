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

# def length(password):
#     if 6 <= len(password) <= 10:
#         return True
#     else:
#         return False
#
#
# def wetters_digits(password):
#     if password.isalnum():
#         return True
#     else:
#         return False
#
#
# def check_for_digit(password):
#     count = 0
#     for i in password:
#         if i.isdigit():
#             count += 1
#     if count < 2:
#         return False
#     else:
#         return True
#
#
# def is_valid(password):
#     is_it = True
#     if not length(password):
#         print("Password must be between 6 and 10 characters")
#         is_it = False
#     if not wetters_digits(password):
#         print("Password must consist only of letters and digits")
#         is_it = False
#     if not check_for_digit(password):
#         print("Password must have at least 2 digits")
#         is_it = False
#     if is_it:
#         print("Password is valid")
#
#
# entry = input()
# is_valid(entry)