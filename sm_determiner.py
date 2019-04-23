from login_with_creds import LoginWithCreds


if __name__ == '__main__':
    sm_type = input('Select a social media(facebok / instagram / twitter): ')
    user_name = input('Enter your username(or email): ')
    password = input('Enter your password: ')
    LoginWithCreds(sm_type, user_name, password)
