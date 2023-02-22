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


if __name__ == '__main__':
    execution_times = {
        "post_image": 12,
        "like_follow_comment": 18,
    }
    while True:
        post_daily_image()
        next_run = 24 * 60 * 60
        time.sleep(next_run)
