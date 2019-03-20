#!/usr/bin/env python3

import argparse
import praw
from datetime import datetime


def authenticate():
    reddit = praw.Reddit(
        'aggregator', user_agent='web:aggregate:v0.1 (by /u/korpog)')
    return reddit


def unix_time_to_utc(unix_time):
    date = datetime.utcfromtimestamp(unix_time).strftime("%d %B %Y %X")
    return date


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get a list of top submissions in a specified subreddit")
    parser.add_argument(
        '--file', help="enabling this flag will write results in an output file", action="store_true")
    parser.add_argument(
        'subreddit', help="name of the subreddit you want to aggregate", type=str)
    parser.add_argument('time', help='''time filter for your query
         (allowed arguments: hour, day, week, month, year, all)''', type=str)
    parser.add_argument(
        'results', help="number of results you want to receive (max=100)", type=int)
    args = parser.parse_args()

    reddit = authenticate()
    if(args.file):
        f = open(f'{args.subreddit}_{args.time}.txt', "w+")
        for stuff in reddit.subreddit(args.subreddit).top(time_filter=args.time, limit=args.results):
            f.write(stuff.title + ' :: ' + unix_time_to_utc(stuff.created_utc) + '\n')
            f.write(stuff.url + '\n')
            f.write('\n')
        f.close()
    else:
        for stuff in reddit.subreddit(args.subreddit).top(time_filter=args.time, limit=args.results):
            print(stuff.title + ' :: ' + unix_time_to_utc(stuff.created_utc) + '\n')
            print(stuff.url)
            print()
