"""

This is a echo bot.

It echoes any incoming text messages.

"""
import wikipedia
wikipedia.set_lang('uz')

import logging


from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5685158664:AAEextmM5IqhQgBb2zgAkzFRF8iTgHtXXUQ'


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Salom Wikipediabotga hush kelibsiz!\n" "Siz bu botga maqola nomini tashlaysiz bot esa sizga maqolani tashlaydi!")




@dp.message_handler()

async def sendWiki(message: types.Message):
    try:
        natija=wikipedia.summary(message.text)
        await message.answer(natija)
    except:
        await message.answer('Bunday maqola topilmadi!')





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)