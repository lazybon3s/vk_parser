# -*- coding: utf-8 -*-

import requests
import csv

# для работы с API вк
ver = 5.92
# offset = 0

# хранилище для постов
posts = []

token = input('Token: ')
group_id = input('ID of group to parse: ')
posts_num = int(input('Number of posts to parse: '))


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
        write = csv.writer(file)
        write.writerow((['text in post']))
        for post in all_posts:
            write.writerow(post['text'])


disparse(posts)

print('File ' + group_id + '.csv was created in script directory, with information about ' + str(posts_num) + ' posts.')
