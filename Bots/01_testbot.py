import telebot
import openai

bot = telebot.TeleBot('5810943249:AAHbif8y0ZMnzcOlqaFuzvLwXrKw68IHmZM')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, ask me a question and I'll do my best to answer it.")


@bot.message_handler(func=lambda message: True)
def get_answer(message):
    question = message.text
    model = "davinci"
    engine = "text-davinci-003"
    openai.api_key = "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"
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
