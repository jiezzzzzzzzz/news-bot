import telebot
import requests
from bs4 import BeautifulSoup
import os
import time

token = os.environ['TOKEN']
bot = telebot.TeleBot(os.getenv('TOKEN'))
channel_id = '@chtotoproishodit'
# сюда можно вставить ссылку на любой канал


url = 'https://vc.ru/new'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
post = soup.find('div', class_="feed__item l-island-round")
title = post.find("div", class_="content-container").text.strip()
post_url = post.find("a", class_="content-link", href=True)["href"].strip()

small_db = []


@bot.message_handler(commands=["start"])
def main(m):
    while True:
        bot.send_message(channel_id, title + post_url)
        small_db.append(post_url)
        if post_url in small_db:
            time.sleep(1800)
        else:
            bot.send_message(channel_id, title + post_url)
            time.sleep(1800)


bot.polling(none_stop=True)

# ссылка на канал, куда отправляются новости - https://t.me/chtotoproishodit
# задеплоено на heroku
