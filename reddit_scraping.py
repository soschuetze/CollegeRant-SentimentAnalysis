import praw
import pandas as pd

# Initialize PRAW with your credentials
reddit = praw.Reddit(
    client_id='oINMc4behxDmx9qWm__9-w',
    client_secret='YJIDQn_oWB1o6cwHDPuz4YX2tkKjqA',
    user_agent='collegerant-sentanalysis'
)

def get_posts(old_df):
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
    new_df = pd.DataFrame(submission_data)

    new_posts = new_df[~new_df['Title'].isin(old_df['Title'])]
            
    # If there are new posts, append them to the existing DataFrame
    if not new_posts.empty:
        df = pd.concat([old_df, new_posts])
    else:
        df = old_df

    df.to_csv("submissions.csv")

# Entry point of the script
if __name__ == "__main__":
    existing_df = pd.read_csv('submissions.csv')
    get_posts(existing_df)