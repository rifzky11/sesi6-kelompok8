def validate_name(name):
    name = name.strip()
    
    if not name:
        return False

    for char in name:
        if not (char.isalpha() or char == ' '):
            return False

    return True



print(validate_name("ipan"))