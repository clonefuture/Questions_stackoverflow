import datetime
import time
import json
import requests
from pprint import pprint


def get_questions(num_of_days, tagged):
    sec = num_of_days * 86400
    date_time = round(time.time() - sec)
    tagged = tagged.lower()

    url = f'https://api.stackexchange.com/2.3/questions?fromdate={date_time}&order=desc&sort=creation&tagged={tagged}&site=stackoverflow'
    resp = requests.get(url)
    dict_question = {}
    i = 1
    for items in resp.json()['items']:
        dict_question[i] = items['title']
        i += 1
    return dict_question


if __name__ == '__main__':
    num_of_days = 2
    tagged = 'Python'
    pprint(get_questions(num_of_days, tagged))
