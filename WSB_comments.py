import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='qxdM8RPWv0PhTw',
                     client_secret='3tDTOoy9yL4e7xZ8-dAspo38bRn7EA',
                     user_agent='linux:pythonForSchool:v1.0.0.0',
                     username='Particular-Tennis-33',
                     password='January94',
                     check_for_async=False)

subreddit = reddit.subreddit('wallstreetbets')
top_subreddit = subreddit.top(limit=10)
print(top_subreddit)

post_dict = {
    "title": [],  # title of the post
    "score": [],  # score of the post
    "id": [],  # unique id of the post
    "url": [],  # url of the post
    "comments_num": [],  # the number of comments on the post
    "created": [],  # timestamp of the post
    "body": []  # the description of post
}

for submission in top_subreddit:
    post_dict["title"].append(submission.title)
    post_dict["score"].append(submission.score)
    post_dict["id"].append(submission.id)
    post_dict["url"].append(submission.url)
    post_dict["comments_num"].append(submission.num_comments)
    post_dict["created"].append(submission.created)
    post_dict["body"].append(submission.selftext)

print(post_dict)
comms_dict = { "post": [], "body":[], "comm_id":[], "created":[] }

iteration = 1
for post in post_dict["id"]:
    print(str(iteration))
    iteration += 1
    submission = reddit.submission(id=post)
    submission.comments.replace_more(limit=2)
    for top_level_comment in submission.comments:
        comms_dict["post"].append(post)
        comms_dict["body"].append(top_level_comment.body)
        comms_dict["comm_id"].append(top_level_comment)
        comms_dict["created"].append(top_level_comment.created)
print("done")

comms_data = pd.DataFrame(comms_dict)
post_data = pd.DataFrame(post_dict)


# get better dates.
def get_date(created):
    return dt.datetime.fromtimestamp(created)


_timestamp = post_data["created"].apply(get_date)
_timestamp_com = comms_data["created"].apply(get_date)

post_data = post_data.assign(timestamp=_timestamp)
comms_data = comms_data.assign(timestamp=_timestamp_com)


comms_data.to_csv("WSB_comments.csv")
post_data.to_csv("WSB_post.csv")
