def check_valid_age(age):
    if type(age) is str:
        try:
            age = int(age)
        except Exception as e:
            print('error casting the age to an int ', e)
            return False

    return False if age < 0 else True
