import tweepy
import time
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def update_status():
    status = "Status otomatis dari GitHub Actions! Waktu saat ini: " + time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        api.update_status(status)
        print("Status berhasil diupdate!")
    except Exception as e:
        print("Gagal update status:", str(e))

if __name__ == "__main__":
    update_status()