from password_generator import PasswordGenerator


pwd = PasswordGenerator()

pwd_min_length = input("What do you want the password's minimum length to be?")
pwd_max_length = input("What do you want the password's maximum length to be?")
pwd_min_upper_case = input("How many characters at the minimum should be uppercase?")
pwd_min_lower_case = input("How many characters at the minimum should be lowercase?")
pwd_min_num = input("How many numbers at the minimum should the passowrd contain?")
pwd_min_spec_char = input("How many characters at the minimum should be special?")

pwd.minlen = int(pwd_min_length)
pwd.maxlen = int(pwd_max_length)
pwd.minuchars = int(pwd_min_upper_case)
pwd.minlchars = int(pwd_min_lower_case)
pwd.minnumbers = int(pwd_min_num)
pwd.minschars = int(pwd_min_spec_char)

print(pwd.generate())