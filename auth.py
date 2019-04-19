# -*- coding: utf-8 -*-

import requests
import csv

# для работы с API вк
ver = 5.92

# хранилище для постов
posts = []

_input = input('Set a group id, number of posts to parse and token. Use space as separator: ')
_input_lst = _input.split()
group_id = _input_lst[0]
posts_num = _input_lst[1]
token = _input_lst[2]




# while offset < posts_num:
response = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': token,
                            'v': ver,
                            'domain': group_id,
                            'count': posts_num
                           # 'offset': offset
                        }
                        )
# offset += 100

posts.extend(response.json()['response']['items'])

# запись информации в csv файл
def disparse(all_posts):
    with open(group_id + '.csv', 'w') as file:
       # write = csv.writer(file)
       # write.writerow((['text in post']))
        for post in all_posts:
            file.write(post['text'])
            file.write("\n")
         # write.writerow(post['text'])


disparse(posts)

print('File ' + group_id + '.csv was created in script directory, with information about ' + str(posts_num) + ' posts.')
