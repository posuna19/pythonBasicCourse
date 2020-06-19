
def validate_name(userName):
    if len(userName) < 3:
        print('The Name is too short. It should be at least 3 characteres long')
    elif len(userName) > 8:
        print('The userName is longer. It should be 8 chars long at maximum')
    else:
        print('Name is correct')


name = 'PEDRO123123'

validate_name(name)

print("big" > "small")
