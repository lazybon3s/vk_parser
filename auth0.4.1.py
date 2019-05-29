import requests
import json
import csv


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

        writer.writerow((data['type'], data['name'], data['description'], data['section'], data['id'], data['first_name'], data['last_name']))


def disparse(post):
    try:
        obj_type = post['type']
    except:
        obj_type = 0

    try:
        obj_name = post['group']['name']
    except:
        obj_name = '?no name?'

    try:
        obj_desc = post['description']
    except:
        obj_desc = '?no description?'

    try:
        obj_section = post['section']
    except:
        obj_section = 0
    try:
        pr_id = post['profile']['id']
    except:
        pr_id = 0
    try:
        pr_fn = post['profile']['first_name']
    except:
        pr_fn = '?no first name?'
    try:
        pr_ln = post['profile']['last_name']
    except:
        pr_ln = '?no last name?'

    data = {
        'type': obj_type,
        'name': obj_name,
        'description': obj_desc,
        'section': obj_section,
        'id': pr_id,
        'first_name': pr_fn,
        'last_name': pr_ln
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


if __name__ == '__main__':
    main()
