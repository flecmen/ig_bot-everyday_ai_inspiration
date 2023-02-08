from instagrapi import Client
import requests
import time
import os
from datetime import datetime
import random
from dotenv import load_dotenv
load_dotenv()

hashtags = ['quote', 'inspiration', 'ai', 'tech']
comments = [
    "This is so inspiring!",
    "Such a great quote!",
    "Love this!",
    "Positive vibes!",
    "So true!",
    "Words to live by!",
    "Amazing insight!",
    "Uplifting!",
    "Thanks for sharing!",
    "This is exactly what I needed today!",
    "So powerful!",
    "Such a motivator!",
    "Great perspective!",
    "Beautiful words!",
    "Awesome!",
    "Fantastic!",
    "Incredible!",
    "Perfectly said!",
    "Positively impacting!",
    "Loving this!",
    "So wise!",
    "Your words are gold!",
    "Truly inspiring!",
    "Thanks for the reminder!",
    "Positive thoughts!",
    "Such an encouragement!",
    "Exactly what I needed to hear!",
    "So uplifting!",
    "Brilliant!",
    "Your posts always brighten my day!",
    "This is what the world needs!",
    "Wise words!",
    "You have a gift with words!",
    "This resonates with me!",
    "Love the positivity!",
    "So inspiring!",
    "You always bring a smile to my face!",
    "Always spreading joy!",
    "Positive energy!",
    "Love the message!",
    "You are amazing!",
    "This quote is everything!",
    "Keep spreading the love!",
    "The world needs more people like you!",
    "You always know how to inspire!",
    "Thanks for being a light in this world!",
    "Such an inspiration!",
    "Keep shining!",
    "Love the positivity you bring!",
    "You always brighten my day!",
    "You have a way with words!",
    "Thank you for spreading joy!",
]


def generate_image():
    print("Generating image...")
    url = 'https://inspirobot.me/api?generate=true'
    response = requests.get(url)
    image_src = response.text
    print("image source: " + image_src)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"img/{today}.jpg"

    if not os.path.exists("img"):
        os.makedirs("img")

    with open(filename, "wb") as f:
        f.write(requests.get(image_src).content)
        print("sucessfully created file " + filename)

    return filename


def post_image(filename):
    client = Client()
    print('loggin in ...')
    client.login(username=os.getenv("INSTAGRAM_USERNAME"),
                 password=os.getenv("INSTAGRAM_PASSWORD"))
    print('logged in')
    client.photo_upload(
        filename,
        "Follow for more daily high quality inspirational quotes." + "#InspirationQuotes #MotivationMonday #QuoteOfTheDay #LifeLessons #PositiveVibes #WordsToLiveBy #MotivationalQuotes #UpliftingThoughts #DailyMotivation #InspiringWords #WordsOfWisdom " +
        "#EverydayAIInspiration #ArtificialIntelligence #AI #MachineLearning #DeepLearning #Tech #AIForGood #AIArt #AIChallenge #AILove #AIAdvancements #AIInnovation #AIEveryday #AIForAll #AIcommunity",
    )
    print('image uploaded successfully')


def post_daily_image():
    filename = generate_image()
    post_image(filename)


def like_follow_comment():
    try:
        hashtag = random.choice(hashtags)
        client = Client()
        client.login(username=os.getenv("INSTAGRAM_USERNAME"),
                     password=os.getenv("INSTAGRAM_PASSWORD"))
        medias = client.hashtag_medias_recent(hashtag, 5)
        print('liking posts ...')
        for i, media in enumerate(medias):
            client.media_like(media.id)
            print(f"Liked post number {i+1} of hashtag {hashtag}")
            if i % 2 == 0:
                client.user_follow(media.user.pk)
                print(f"Followd user {media.user.username}")
                time.sleep(2)
                client.media_comment(media.id, random.choice(comments))
                print("Commented {comment} under post number {i+1}")
            time.sleep(5)
    except:
        print('like_follow_commnet, failed, nevermind')


if __name__ == '__main__':
    execution_times = {
        "post_image": 12,
        "like_follow_comment": 18,
    }
    while True:
        current_time = time.localtime()
        # ve 12:00
        if current_time.tm_hour == 12:
            post_daily_image()
            next_run = 4 * 60 * 60
        # v 18:00
        elif current_time.tm_hour == 18:
            like_follow_comment()
            next_run = 18 * 60 * 60
        else:
            # Calculate time to the next scheduled run (noon or 6 PM)
            next_noon = 12 - current_time.tm_hour
            if next_noon <= 0:
                next_noon = abs(next_noon)+12
            next_6pm = 18 - current_time.tm_hour
            if next_6pm <= 0:
                next_6pm += abs(next_6pm)+18
            next_run = min(next_noon, next_6pm) * 60 * 60
        # Wait for the calculated time to the next run
        time.sleep(next_run)
