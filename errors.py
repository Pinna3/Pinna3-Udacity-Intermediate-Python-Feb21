INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class PasswordError(ValueError):
    pass

def validate_password(username, password):
    if password != username and password not in INVALID_PASSWORDS:
        return True
    else:
        raise ValueError


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        valid = validate_password(username, password)
    except ValueError:
        raise PasswordError('Pick another password.')
    else:
        account = create_account(username, password)


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!
