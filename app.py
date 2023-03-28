from instagrapi import Client
import requests
import time
import os
from datetime import datetime
import random
from dotenv import load_dotenv
load_dotenv()

hashtags = ['quote', 'inspiration', 'ai', 'tech']


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


def delete_image_locally(filename):
    print('deleting image ' + filename + ' locally')
    os.remove(filename)
    print('image deleted successfully')


def post_daily_image():
    filename = generate_image()
    post_image(filename)
    time.sleep(30)
    delete_image_locally(filename)


if __name__ == '__main__':
    execution_times = {
        "post_image": 12,
        "like_follow_comment": 18,
    }
    while True:
        post_daily_image()
        next_run = 24 * 60 * 60
        time.sleep(next_run)
