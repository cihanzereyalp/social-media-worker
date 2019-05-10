from .login_with_creds import LoginWithCreds


def get_inputs():
    sm_type = input('Select a social media(facebok / instagram / twitter): ')
    user_name = input('Enter your username(or email): ')
    password = input('Enter your password: ')
    if sm_type and user_name and password:
        return sm_type, user_name, password


def start():
    sm_type, user_name, password = get_inputs()
    LoginWithCreds(sm_type, user_name, password)
