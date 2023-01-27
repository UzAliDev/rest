import logging 

from aiogram import Bot, Dispatcher, executor, types
from database import Database

import time

API_TOKEN = '5838623009:AAGbJXn_0CQFQUXTV3X2P8r9NGNrXU8XHmM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

db = Database('database.db')

@dp.message_handler(commands=['start'])

async def start_command(message: types.Message):

    db.create_table_users()

    if(not db.add(message.from_user.id)):
        db.add_id_user_name_data(user_id=message.from_user.id, username=message.from_user.username, first_name=message.from_user.first_name, data=time.ctime())
        await bot.send_message(message.from_user.id, 'Assalomu alaykum')

    else:
        await bot.send_message(message.from_user.id, 'Start bosdingiz {}'.format(message.from_user.get_mention(as_html=True)))


@dp.message_handler(commands=['count'])

async def count(message: types.Message):
    d = db.count()
    await bot.send_message(message.from_user.id, 'Foydalanuvchilar soni {} ta'.format(d))

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)