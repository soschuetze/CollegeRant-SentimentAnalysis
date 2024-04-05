import praw
import pandas as pd

# Initialize PRAW with your credentials
reddit = praw.Reddit(
    client_id='#######',
    client_secret='########',
    user_agent='collegerant-sentanalysis'
)

def get_posts():
    '''
    Obtains submissions and outputs to csv file

    ##Parameters:
    subreddit_name: name of subreddit to obtain posts from
    '''
    # Get the subreddit object
    subreddit = reddit.subreddit('CollegeRant')

    # List to store submission data
    submission_data = []

    # Iterate through submissions
    for submission in subreddit.new(limit=None):  # 'limit=None' will retrieve all submissions
        submission_data.append({
            "Title": submission.title,
            "Score": submission.score,
            "Body": submission.selftext,
            "Author": str(submission.author)  # Convert to string to handle potential None values
        })

    # Create a DataFrame
    df = pd.DataFrame(submission_data)

    df.to_csv("submissions.csv")

# Entry point of the script
if __name__ == "__main__":
    get_posts()