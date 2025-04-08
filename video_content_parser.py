import re
from urllib.parse import urlparse


def video_content_parser(video_link):
    parsed = urlparse(video_link)
    query = parsed.query
    matched = re.findall(r'v=(\w+)', query)
    video_ids = []
    if len(matched) == 1:
        video_ids += matched[0],

    return video_ids
