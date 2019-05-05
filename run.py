from random import randint
from time import sleep
import json

hashtag_url = 'https://www.instagram.com/explore/tags/'
hashtag_list = ['music', 'happy']
xpath_selectors = {}


def load_xpath_selectors():
    global xpath_selectors
    with open("./xpath_selectors.json", 'r') as f:
        xpath_selectors = json.load(f)


def post_to_click(row, column):
    return xpath_selectors.get('hash_tags_post').format(row=row, column=column)


def post_loop(browser):

    follow_xpath = xpath_selectors.get('follow')
    next_xpath = xpath_selectors.get('next_arrow')

    for idx, hashtag in enumerate(hashtag_list):
        browser.get("%s%s/" % (hashtag_url, hashtag))
        sleep(5)
        for i in range(1, 30):
            # drver.find_element_by_xpath(post_to_click(idx + 1, i)).click()
            if i == 1:
                browser.find_element_by_xpath(post_to_click(1, 1)).click()
            sleep(randint(1, 3))
            browser.find_element_by_xpath(follow_xpath).click()
            browser.find_element_by_xpath(next_xpath).click()
