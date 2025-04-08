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
    video_ids = []
    try:
        video_id = json_dict['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonViewModel']['likeButtonViewModel']['likeButtonViewModel']['toggleButtonViewModel']['toggleButtonViewModel']['defaultButtonViewModel']['buttonViewModel']['onTap']['serialCommand']['commands'][1]['innertubeCommand']['modalEndpoint']['modal']['modalWithTitleAndButtonRenderer']['button']['buttonRenderer']['navigationEndpoint']['signInEndpoint']['nextEndpoint']['likeEndpoint']['target']['videoId']

        video_ids = [video_id]
    except Exception as e:
        print(e)
        pass

    return video_ids
