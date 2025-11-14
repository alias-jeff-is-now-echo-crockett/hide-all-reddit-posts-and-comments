import praw
from datetime import datetime, timezone
import time
import prawcore
from reddit_utils import reddit

USERNAME = "big_guyforyou"  # Replace with your username

# Hide anything created before this date:
CUTOFF = datetime(2025, 11, 14, tzinfo=timezone.utc)

###############################################
# Convert Reddit UTC timestamp → Python datetime
###############################################
def utc_timestamp_to_dt(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc)

###############################################
# Rate-limit-safe hide function
###############################################
def hide_with_retry(thing):
    while True:
        try:
            thing.hide()
            return True

        except prawcore.exceptions.TooManyRequests as e:
            wait = getattr(e, "sleep_time", None)
            if wait is None:
                wait = 10
            print(f"⚠️ Rate limited. Sleeping {wait} seconds...")
            time.sleep(wait)

        except Exception as e:
            print(f"❌ Error hiding {thing.id}: {e}")
            return False


###############################################
# Hide old submissions
###############################################
def hide_old_submissions(reddit):
    print("Checking submissions…")
    me = reddit.redditor(USERNAME)

    for submission in me.submissions.new(limit=None):
        created_dt = utc_timestamp_to_dt(submission.created_utc)

        if created_dt < CUTOFF:
            if hide_with_retry(submission):
                print(f"✔ HIDDEN POST: {submission.id} ({created_dt})")


###############################################
# Hide old comments
###############################################
def hide_old_comments(reddit):
    print("Checking comments…")
    me = reddit.redditor(USERNAME)

    for comment in me.comments.new(limit=None):
        created_dt = utc_timestamp_to_dt(comment.created_utc)

        if created_dt < CUTOFF:
            if hide_with_retry(comment):
                print(f"✔ HIDDEN COMMENT: {comment.id} ({created_dt})")


###############################################
# MAIN
###############################################
if __name__ == "__main__":
    print(f"Running hide script for u/{USERNAME}…")
    print(f"Hiding anything created BEFORE {CUTOFF}")



    hide_old_submissions(reddit)
    hide_old_comments(reddit)

    print("Done!")
