import jokeSender
import requests
import datetime
import time

Time = datetime.datetime


def get_joke():
    global Time
    day = Time.today()
    day = day.date()
    response = requests.get(url="https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,sexist&format=txt")
    joke = f"Subject: Joke of the day! {day} \n\n {response.text}"
    return joke


def send_joke():
    joke_sender = jokeSender.Mailer()
    joke_sender.send("souryachoudhury24@gmail.com", get_joke())


while True:

    current_hour = Time.now().hour
    if current_hour == 20:
        send_joke()

    time.sleep(3600)





