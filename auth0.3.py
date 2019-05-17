import requests
import json
import time
import csv

#6c0a9f018ab961d9eacc4e144b34d15876181accddfe1c84665ef7cffd8e2e3d4c8e902afaa1f780705ad

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

        writer.writerow((data['type'], data['name'], data['description']))


def disparse(post):
    try:
        obj_type = post['type']
    except:
        obj_type = 0

    try:
        obj_name = post['group']['name']
    except:
        obj_name = 'xxx'

    try:
        obj_desc = post['description']
    except:
        obj_desc = 'no description'

    try:
        obj_section = post['section']
    except:
        obj_section = 0



    data = {
        'type': obj_type,
        'name': obj_name,
        'description': obj_desc,
        'section': obj_section
    }

    return data

def main():
    ver = 5.92
    _input = input('Set a request, number of responses and token. Use slash as separator: ')
    _input_lst = _input.split('/')
    request = _input_lst[0]
    limit = _input_lst[1]
    token = _input_lst[2]


    response = requests.get('https://api.vk.com/method/search.getHints',
                            params={
                                    'access_token': token,
                                    'v': ver,
                                    'q': request,
                                    'limit': limit,
                                    'search_global': 1
                                    })
    posts = response.json()['response']['items']
    print('Number of parsed posts: ' + str(len(posts)))

    for post in posts:
        post_data = disparse(post)
        to_csv(post_data)
        to_json(post_data)
        print(len(post_data))

    print(len(posts))


if __name__ == '__main__':
    main()
