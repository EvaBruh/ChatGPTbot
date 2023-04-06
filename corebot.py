from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import openai

openai.api_key = "sk - S7z5d5Rxs9uymT6chmelT3BlbkFJmKa403Hcfhz20SViju1i"  # Установите свой ключ API OpenAI здесь

updater = Updater(token='6099500538:AAEchBogjIiFhpgUY70qZhOIV6Eyptum83s', use_context=True)  # Установите свой токен API Telegram здесь


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your personal bot.')


start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)


def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text

    # Используйте chatGPT для генерации ответа на сообщение пользователя
    response = openai.Completion.create(
        #engine="davinci",
        model="gpt-3.5-turbo",
        #prompt=user_message,
        #temperature=0.7,
        #max_tokens=150,
        #top_p=1,
        #frequency_penalty=0,
        #presence_penalty=0
    )
    bot_response = response['choices'][0]['text']
    update.message.reply_text(bot_response)


message_handler = MessageHandler(filters.TEXT & ~filters.Command, handle_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()