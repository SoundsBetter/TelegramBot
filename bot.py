import telebot
import openai
import os

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, ask me a question and I'll do my best to answer it.")

@bot.message_handler(func=lambda message: True)
def get_answer(message):
    question = message.text
    model = "davinci"
    engine = "text-davinci-003"
    openai.api_key = os.environ['OPENAI_API_KEY']
    completion = openai.Completion.create(
        engine=engine,
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = completion.choices[0].text.strip()
    bot.reply_to(message, answer)

bot.polling()