import argparse
import os
import time

import handler

def print_topics():
    print('Available BBC topics:')
    for topic in BBS_TOPICS:
        print(f'[\033[32m#\033[0m] {topic}')
        time.sleep(0.1)

def main():
    parser = argparse.ArgumentParser(
        description='BBC News RSS Parser'
    )

    # https://github.com/python/cpython/issues/101337
    # https://stackoverflow.com/questions/17909294/argparse-mutual-exclusive-group
    # https://docs.python.org/3/library/argparse.html
    mode = parser.add_mutually_exclusive_group(required=True)

    mode.add_argument('-l', '--list-topics', action='store_true', help='Show available BBC topics')
    mode.add_argument('-p', '--parse', type=str, help='Parse BBC topic (default: Top_Stories)')
    mode.add_argument('--parse-all', action='store_true', help='Parse all BBC topics')

    parser.add_argument('--limit', type=int, default=None, help='Limit number of parsed news')
    parser.add_argument('-o', '--output', type=str, default='./data', help='Output directory')

    args = parser.parse_args()
    print(args)

    if args.list_topics:
        handler.handle_list_topics()
    elif args.parse:
        handler.handle_parse(args.parse, args.limit, args.output)
    elif args.parse_all:
        handler.handle_parse_all(args.limit, args.output)

if __name__ == '__main__':
    main()
