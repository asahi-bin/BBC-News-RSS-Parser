import os
import time

from config import BBS_TOPICS
from fetcher import fetch_page
from parser import parse_news
from storage import save_to_json

def handle_list_topics():
    print('Available BBC topics:')
    for topic in BBS_TOPICS:
        print(f'[\033[32m#\033[0m] {topic}')
        time.sleep(0.1)

def handle_parse(topic, limit, output):
    if topic not in BBS_TOPICS:
        print('\033[31mUnknown topic\033[0m')
        return

    # https://www.geeksforgeeks.org/python/python-os-makedirs-method/
    os.makedirs(output, exist_ok=True)

    url = BBS_TOPICS[topic]
    html = fetch_page(url)
    news = parse_news(html, limit=limit)
    save_to_json(
        news,
        f'{output}/{topic}.json',
        topic
    )
    print(f'[\033[32m+\033[0m] Parsing {topic}')

def handle_parse_all(limit, output):
    os.makedirs(output, exist_ok=True)

    for topic, url in BBS_TOPICS.items():
        html = fetch_page(url)
        news = parse_news(html, limit=limit)
        save_to_json(
            news,
            f'{output}/{topic}.json'
        )
        print(f'[\033[32m+\033[0m] Parsing {topic}')
        time.sleep(0.05)
