from aiogram import types, Bot, Dispatcher, executor
from data import Api_token
# from buttons import
from inline_buttons import menuMain, asosiymenu

bot = Bot(token=Api_token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_handler(message:types.Message):
    await message.answer_photo("https://t.me/holdikshop/6","Добро пожаловать в магазин гемов Holdik Gems\nhttps://t.me/holdikshop""\nВоспользуйся меню👇",reply_markup=menuMain)

@dp.message_handler(commands="help")
async def start_handler(message:types.Message):
    await message.answer("Если вам не пришли гемы или хотите отменить заказ и вам нужно какой то помощь то пишите в поддержку.\nИ вам ответят и помогут.")

@dp.message_handler(text="coursec")
async def start_handler(message:types.Message):
    await message.answer_photo("https://t.me/holdikshop/177","Список товаров 👇",reply_markup=asosiymenu)



if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)    