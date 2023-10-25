import requests
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
channel_name_url = 'https://www.youtube.com/' + channel_name
ifttt_event_url = config[need_keys[0]]

if 'hqdefault_live.jpg' in response.text:
    requests.get(ifttt_event_url)
    print('Sending the %s is done!' % ifttt_event_url)


print('Checking is done!')
