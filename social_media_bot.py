import os
from selenium import webdriver
from sm_data import SmData
from time import sleep


class SmEngine():
    def __init__(self, sm_type="instagram"):
        self.data = SmData()
        self.sm_type = sm_type
        self.selected_sm = self.data.sm_info.get(sm_type)

        self.driver_path = os.path.expanduser(r'~\Downloads\chromedriver_win32\chromedriver.exe')
        self.browser = webdriver.Chrome(executable_path = self.driver_path)
        sleep(2)
