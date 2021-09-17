import logging
import os
import re

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

load_dotenv()

PROXY = {
    'proxy_url': os.getenv('PROXY_URL'),
    'urllib3_proxy_kwargs': {
        'username': os.getenv('PROXY_USERNAME'),
        'password': os.getenv('PROXY_PASSWORD')
    }
}


def greet_user(update, context):
    text = '''Это бот подсчета слов! Введите /wordcount <sentence> и узнаете\
     количество слов в предложении'''
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_word_count(update, context):
    raw_string = update.message.text
    clear_raw = re.sub("\s\s+", " ", raw_string.strip())
    clear_raw = clear_raw.split()[1:]
    if not clear_raw:
        update.message.reply_text("введите предложение в формате /wordcount <sentence>")
    else:
        string = f"количество слов в предложении:{len(clear_raw)}"
        update.message.reply_text(string)


def main():
    count_word_bot = Updater(os.getenv('KEY'),
                             request_kwargs=PROXY, use_context=True)

    dp = count_word_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", get_word_count))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    count_word_bot.start_polling()
    count_word_bot.idle()


if __name__ == "__main__":
    main()
