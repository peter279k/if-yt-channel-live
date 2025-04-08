import os
import requests
from bs4 import BeautifulSoup
import video_content_parser
from dotenv import dotenv_values


config = dotenv_values('./.env')
config_keys = list(config.keys())
need_keys = [
    'ifttt_service_url', 'channel_name',
]
for need_key in need_keys:
    if need_key not in config_keys:
        raise Error('%s is not found in .env file!' % need_key)


channel_name = config[need_keys[1]]
channel_name_url = 'https://www.youtube.com/' + channel_name + '/live'
ifttt_event_url = config[need_keys[0]]

response = requests.get(channel_name_url)
soup = BeautifulSoup(response.text, 'html.parser')
video_link = soup.select('link[rel="canonical"]')
if len(video_link) == 1:
    requests.get(ifttt_event_url)
    print('Sending the %s is done!' % ifttt_event_url)
    video_ids = video_content_parser.video_content_parser(video_link[0])
    yt_path = './yt_video_ids.txt'
    contents = ''
    if os.path.isfile(yt_path) is True:
        with open(yt_path, encoding='utf-8', mode='r') as f:
            contents = f.read()

    with open(yt_path, encoding='utf-8', mode='a') as f:
        for video_id in video_ids:
            if video_id in contents:
                continue

            f.write(video_id + '\n')

    print('The YouTube video id text file is saved.')

print('Checking is done!')
