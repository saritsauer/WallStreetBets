#!pip install praw

import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='qxdM8RPWv0PhTw', 
                     client_secret='3tDTOoy9yL4e7xZ8-dAspo38bRn7EA', 
                     user_agent='linux:pythonForSchool:v1.0.0.0', 
                     username='Particular-Tennis-33', 
                     password='****ar***',
                     check_for_async=False)

subreddit = reddit.subreddit('wallstreetbets')
top_subreddit = subreddit.top(limit=1000)
print(top_subreddit)

topics_dict = { 'title':[], 
                'score':[], 
                'id':[], 'url':[], 
                'comms_num': [], 
                'created': [], 
                'body':[]
               }

for submission in top_subreddit:
    topics_dict['title'].append(submission.title)
    topics_dict['score'].append(submission.score)
    topics_dict['id'].append(submission.id)
    topics_dict['url'].append(submission.url)
    topics_dict['comms_num'].append(submission.num_comments)
    topics_dict['created'].append(submission.created)
    topics_dict['body'].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
print(topics_data)

### get better dates.
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)
print(topics_data)


topics_data.to_csv('wallstreetbet.csv', index=False) 