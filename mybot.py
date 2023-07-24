from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Бот реагирует на определенные команды в чате
@dp.message_handler(commands=['start', 'welcome', 'about'])
async def cmd_handler(message: types.Message):
    await message.answer('its help bot')

# Бот реагирует на наличие определенной фразы в чате (в том числе в исправленном сообщении)
@dp.message_handler(lambda message: message.text and 'hello' in message.text.lower())
@dp.edited_message_handler(lambda message: message.text and 'hello' in message.text.lower())
async def msg_handler(message: types.Message):
    await message.answer('И тебе привет')

# Бот реагирует на изображения в чате
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def audio_handler(message: types.Message):
    await message.answer('Крутая фотка')

# Бот возвращает написанное обратно в чат
@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)