import telebot
import requests

bot = telebot.TeleBot('5822043807:AAFGheJnFmoP0Hq_8Hql7osemkIaqabNx-c')

database_id = 'https://www.notion.so/amazigh-brewing-company/d17efb58698d429ab4f77a3f75846898?v=6a848ec256804800b966e7251051d8ef'
api_key = 'secret_qoJBmRrzH388ccyQ6T4xd2Sd4BDmG84hUlQ5b3Yh3ny'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для сохранения ваших расходов. Пожалуйста, отправьте мне сумму расхода, дату операции, примечания и бюджет в формате: /expense sum date notes budget")

@bot.message_handler(commands=['expense'])
def add_expense(message):
    try:
        text = message.text.split(' ')
        if len(text) != 5:
            bot.reply_to(message, "Неверный формат. Пожалуйста, используйте формат: /expense sum date notes budget")
            return

        expense_data = {
            "sum": {
                "title": [
                    {
                        "text": {
                            "content": text[1]
                        }
                    }
                ]
            },
            "date": {
                "date": {
                    "start": text[2],
                    "end": None
                }
            },
            "notes": {
                "rich_text": [
                    {
                        "text": {
                            "content": text[3]
                        }
                    }
                ]
            },
            "budget": {
                "select": {
                    "name": text[4]
                }
            }
        }

        headers = {
            'Content-Type': 'application/json
