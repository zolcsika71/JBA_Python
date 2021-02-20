def check_email(string):
    if ' ' in string or '.@' in string or '@.' in string:
        return False
    elif '@' not in string or '.' not in string:
        return False
    elif '.' not in string[string.find('@') + 1:]:
        return False
    else:
        return True
