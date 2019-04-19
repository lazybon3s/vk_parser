# -*- coding: utf-8 -*-

import requests
import json
import time
import csv
from datetime import datetime


def write_json(data):
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def to_json(post_dict):
    try:
        data = json.load(open('posts_data.json', encoding='utf-8'))
    except:
        data = []

    data.append(post_dict)

    with open('posts_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def to_csv(data):
    with open('posts_data.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow((data['id'], data['text']))


def disparse(post):
    try:
        post_id = post['id']
    except:
        post_id = 0

    try:
        text = post['text']
    except:
        text = 'xxx'

    try:
        likes = post['likes']['count']
    except:
        likes = 0

    try:
        reposts = post['reposts']['count']
    except:
        reposts = 0



    data = {
        'id': post_id,
        'text': text,
        'likes': likes,
        'reposts': reposts
    }

    return data

def main():
    ver = 5.92
    _input = input('Set a group id, number of posts to parse and token. Use space as separator: ')
    _input_lst = _input.split()
    group_id = _input_lst[0]
    posts_num = _input_lst[1]
    token = _input_lst[2]
#    offset = 0

#    timestamp = int(time.time())
#    print(timestamp)
    all_posts = []

    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                    'access_token': token,
                                    'v': ver,
                                    'domain': group_id,
                                    'count': posts_num
                                    })
    posts = response.json()['response']['items']

#    all_posts.extend(posts)

#    oldest_post_date = posts[-1]['date']

#    offset += 100
#    print(offset)

#        if oldest_post_date < timestamp:
#           break

    print('Number of parsed posts: ' + str(len(posts)))

    for post in posts:
        post_data = disparse(post)
        to_csv(post_data)
        to_json(post_data)
        print(len(post_data))

    print(len(posts))


if __name__ == '__main__':
    main()
