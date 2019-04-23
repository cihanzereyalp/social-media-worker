from time import sleep
from social_media_bot import SmEngine
from popup_ignore import ignore_notification


class LoginWithCreds(SmEngine):
    def __init__(self, sm_type, user_name, password):
        super(LoginWithCreds, self).__init__(sm_type)
        self.username = user_name
        self.password = password
        self.load_web_page()
        self.fill_and_login()

    def load_web_page(self):
        self.browser.get(self.selected_sm.get('login_url'))
        sleep(2)

    def fill_and_login(self):
        username = self.browser.find_element_by_name('username')
        username.send_keys(self.username)

        password = self.browser.find_element_by_name('password')
        password.send_keys(self.password)

        button_login = self.browser.find_element_by_css_selector('button[type="submit"]')
        button_login.click()
        sleep(3)
        ignore_notification(self.browser)
