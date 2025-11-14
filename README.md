#README — Hide Old Reddit Posts & Comments

This script automatically hides all of your own Reddit submissions and comments created before a specific date.
It is designed for personal privacy cleanup, letting you bulk-hide older Reddit history safely while respecting Reddit’s API rate limits.

#FEATURES

Hide old submissions (posts)

Hide old comments

Handles Reddit rate limiting automatically

Custom cutoff date

Uses Reddit’s official API (PRAW)

Useful for privacy cleanups and account resets

#REQUIREMENTS

Python 3.8 or newer

Virtual environment recommended

PRAW installed:

pip install praw

#SETUP INSTRUCTIONS

Create a Reddit “script” app at:
https://www.reddit.com/prefs/apps

Copy the following values from your app page:

client_id

client_secret

Reddit username

Reddit password

Optional: your own user-agent string

Insert these values into the script:

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
USERNAME = "type your username inside the quotation marks right here"
PASSWORD = "type your password here inside the quotes while your'e at it"
USER_AGENT = "hide-old-content-script by /u/big_guyforyou"

Set the cutoff date.
Any post or comment created before this timestamp will be hidden:

CUTOFF = datetime(2025, 11, 1, tzinfo=timezone.utc)

USAGE

Run the script using your virtual environment:

~/new_python/venv/bin/python hide_old_content.py


The script will automatically:

Fetch your posts

Fetch your comments

Hide content older than the cutoff date

Respect Reddit’s 429 Too Many Requests rate limit

Print actions as it runs, for example:

✔ HIDDEN POST: abc123 (2025-08-12 09:40:30+00:00)
⚠️ Rate limited. Sleeping 7 seconds...
✔ HIDDEN COMMENT: def456 (2025-07-02 11:20:18+00:00)

HOW IT WORKS

Logs into Reddit using PRAW.

Retrieves all of your posts and comments.

Converts Reddit’s UTC timestamps to Python datetime objects.

Compares each timestamp to the cutoff date.

Hides qualifying items using a safe “retry if rate limited” function.

Waits the correct number of seconds if Reddit issues a 429 response.

IMPORTANT NOTES

You can only hide your own posts and comments (Reddit restriction).

Hidden items are reversible in your account.

This script does not delete anything.
(A delete mode can be added if needed.)

If your account has a large history, the process may take time due to rate limits.

OPTIONAL IMPROVEMENTS AVAILABLE

I can generate upgraded versions that include:

Dry-run mode (preview changes without hiding anything)

JSON or CSV logging

Unhide mode

Delete mode (with double confirmation)

Progress bar

Automatic resume if script stops

Filtering by subreddit

LICENSE

This tool is intended for personal use.
Use responsibly and in accordance with Reddit’s API rules.
