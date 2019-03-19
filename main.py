import sys
import praw

def authenticate():
    reddit = praw.Reddit('aggregator', user_agent = 'web:aggregate-wn:v0.1 (by /u/korpog)')
    return reddit

def main(subreddit, num_results):
    reddit = authenticate()
    for stuff in reddit.subreddit(subreddit).top(time_filter='day', limit=num_results):
        print(stuff.title)
        print(stuff.url)
        print()

if __name__ == "__main__":
    subreddit = sys.argv[1]    
    num_results = (int)(sys.argv[2])    
    main(subreddit, num_results)

