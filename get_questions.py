import datetime
import time
import json
import requests
from pprint import pprint


def get_questions(num_of_days, tagged):
    list_question = []
    sec = num_of_days * 86400
    date_time = round(time.time() - sec)
    tagged = tagged.lower()

    url = 'https://api.stackexchange.com/2.3/questions?&order=desc&sort=creation&site=stackoverflow'
    x = 0
    has_more = True
    while has_more is True:
        x += 1
        params = {'page': x, 'pagesize': 100, 'fromdate': date_time, 'tagged': tagged}
        resp = requests.get(url, params=params)
        for items in resp.json()['items']:
            list_question.append(items['title'])
        has_more = resp.json()['has_more']
    dict_questions = {}
    x = 1
    for i in list_question:
        dict_questions[x] = i
        x += 1
    return dict_questions


if __name__ == '__main__':
    num_of_days = 2
    tagged = 'Python'
    pprint(get_questions(num_of_days, tagged))
