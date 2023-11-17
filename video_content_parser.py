import json
from bs4 import BeautifulSoup


def video_content_parser(contents):
    json_data_keyword = 'var ytInitialData = '
    soup = BeautifulSoup(contents, 'html.parser')
    scripts = soup.select('script')
    json_content = None
    for script in scripts:
        if json_data_keyword in script.text:
            json_content = script.text
            break

    if json_content is None:
        print('Cannot find the JSON contents')
        exit(0)


    json_content = json_content.replace(json_data_keyword, '')
    json_content = json_content[0:-1]

    json_dict = json.loads(json_content)
    video_contents = json_dict['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

    video_ids = []
    video_ids_append = video_ids.append
    video_info = video_contents[0]
    if 'channelFeaturedContentRenderer' not in [*video_info.keys()]:
        return video_ids


    video_items = video_info['channelFeaturedContentRenderer']['items']
    for video_item in video_items:
        video_ids_append(video_item['videoRenderer']['videoId'])


    return video_ids
