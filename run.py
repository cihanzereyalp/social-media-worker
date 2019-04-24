from random import randint
from time import sleep

hashtag_url = 'https://www.instagram.com/explore/tags/'
hashtag_list = ['music', 'happy']

post_xpath = '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[{row}]/div[{column}]/a/div'


def post_to_click(row, column):
    return post_xpath.format(row=row, column=column)


def post_loop(drver):
    for idx, hashtag in enumerate(hashtag_list):
        drver.get("%s%s/" % (hashtag_url, hashtag))
        sleep(5)
        for i in range(1, 4):
            drver.find_element_by_xpath(post_to_click(idx + 1, i)).click()
            # TODO cant click others without closing first post
            sleep(randint(1, 3))
