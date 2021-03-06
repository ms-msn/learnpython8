from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def main():
    updater = Updater("540429828:AAEj5WiGOKNyn0i_UcdwbVpdJZ-RSktC-ng")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

def talk_to_me(bot, update):
	
    user_text = update.message.text
    user_text = user_text.lower()
    answer = answers[user_text]
    print(user_text)
    update.message.reply_text(answer)

main()