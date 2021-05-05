import tweepy
from os import listdir
from os.path import isfile, join
from random import randrange


def main():
    twitter_auth_keys = {
        "consumer_key": "YOUR_CONSUMER_KEY",
        "consumer_secret": "YOUR_SECRET_KEY",
        "access_token": "YOUR_TOKEN",
        "access_token_secret": "YOUR_SECRET_TOKEN"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    # Pick a image
    media = api.media_upload(pick_image())

    # Post tweet with image
    tweet = ""
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])


def pick_image():
    """Make a list with the files on the folder that you choose,
    then pick a random image."""
    only_files = [f for f in listdir('./images') if isfile(join('./images', f))]
    i = randrange(0, len(only_files), 2)
    return f'./images/{only_files[i]}'


if __name__ == "__main__":
    main()