import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Your token should be here'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)










if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)