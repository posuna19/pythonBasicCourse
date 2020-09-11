def validate_user(username, minlen):
    assert type(username) == str, "username musth be a string"

    if minlen < 1:
        raise ValueError("minlen parameter must be at least 1")

    if len(username) < minlen:
        return False

    if not username.isalnum():
        return False

    return True


#print(validate_user("Laura", -1))
#print(validate_user("Lau", 0))