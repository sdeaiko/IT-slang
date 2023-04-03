import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import __API_TOKEN__
from data import lists, word_search

logging.basicConfig(level=logging.INFO)

bot = Bot(token=__API_TOKEN__)
dp = Dispatcher(bot)


l1, l2, l3, l4, l5 = KeyboardButton('А'), KeyboardButton('Б'), KeyboardButton('В'), KeyboardButton('Г'), KeyboardButton('Д')

l6, l7, l8, l9, l10 = KeyboardButton('Е'), KeyboardButton('Ж'), KeyboardButton('З'), KeyboardButton('И'), KeyboardButton('К')

l11, l12, l13, l14, l15 = KeyboardButton('Л'), KeyboardButton('М'), KeyboardButton('Н'), KeyboardButton('О'), KeyboardButton('П')

l16, l17, l18, l19, l20 = KeyboardButton('Р'), KeyboardButton('С'), KeyboardButton('Т'), KeyboardButton('У'), KeyboardButton('Ф')

l21, l22, l23, l24, l25 = KeyboardButton('Х'), KeyboardButton('Ц'), KeyboardButton('Ч'), KeyboardButton('Ш'), KeyboardButton('Э')

l26, l27 = KeyboardButton('Ю'), KeyboardButton('Я')

btn_cancel = KeyboardButton('Назад')


kb = ReplyKeyboardMarkup(resize_keyboard=True)


kb.row(l1, l2, l3, l4, l5).row(l6, l7, l8, l9, l10).row(l11, l12, l13, l14, l15).row(l16, l17, l18, l19, l20).row(l21, l22, l23, l24, l25).row(l26, l27).row(btn_cancel)

btn_search = KeyboardButton('Поиск🔎')
btn_alphabet = KeyboardButton('Поиск по алфавиту🔠')
btn_help = KeyboardButton('Информация о боте')
btn_contacts = KeyboardButton('Контакты📞')
kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start.add(btn_search, btn_alphabet).row(btn_help).row(btn_contacts)

msg = 'Добро пожаловать в наш поисковый бот для IT сленга 💻 ! Наш бот разработан для того, чтобы помочь вам ориентироваться в постоянно развивающемся мире IT-жаргона 💬 . С помощью простого поиска 🔍  и аббревиатурам 💡 . Больше никакой путаницы на встречах или обсвы можете найти пояснения к последним техническим терминамуждениях 🤯 , наш бот вас доступен в любое время💪 . Являетесь ли вы опытным ИТ-специалистом 💼 или только начинаете , наш бот - ценный ресурс 💰 . Просто введите нужное вам жаргонное слово 🔎 , и наш бот предоставит вам четкое и лаконичное определение 💬 . Попробуйте это прямо сейчас! 🚀'

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 
                        msg, reply_markup=kb_start)

@dp.message_handler()
async def echo(message: types.Message):
    
    word = message.text
    
    if word == 'Поиск🔎':
        await bot.send_message(message.from_user.id, 'Дорогой пользователь, для того, чтобы найти нужное вам слово, напишите: \n\n/s (нужное вам слово)\n\nК примеру, /s нуб')
        
    if word == 'Поиск по алфавиту🔠':
        await bot.send_message(message.from_user.id, 'Алфавит:', reply_markup=kb)
        
    if word == 'Информация о боте':
        await bot.send_message(message.from_user.id, msg)
        
    if word == 'Контакты📞':
        await bot.send_message(message.from_user.id, 'По всем вопросам - https://t.me/snurmuhambet')
        await bot.send_message(message.from_user.id, 'По всем вопросам - https://t.me/Dinara37')
        await bot.send_message(message.from_user.id, 'По всем вопросам - https://t.me/goldenxeo')
        await bot.send_message(message.from_user.id, 'По всем вопросам - https://t.me/auezkuanbekov')
        
    if word == 'Назад':
        await bot.send_message(message.from_user.id, 'главное меню: ', reply_markup=kb_start)
        
        
        
    if '/s' in word:
        await message.answer(word_search(word[3:]))
        
    letters = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЭЮЯ"
    
    if len(word) == 1 and word in letters:
        index = letters.index(word)
        for i in range(len(lists[index])):
            await message.answer(lists[index][i])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)