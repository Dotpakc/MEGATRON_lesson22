import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5915096811:AAHjLrgLbKhemHt8x66w3uQWxehjB5KRQN4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

users_colors = {1: ['red', 'green', 'blue'], 2: ['yellow', 'black', 'white']}
color_list = ['red', 'green', 'blue', 'yellow', 'black', 'white', 'pink', 'purple', 'orange', 'brown', 'gray', 'cyan']


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")





@dp.message_handler(commands=['colors'])
async def send_colors(message: types.Message):
    if users_colors.get(message.from_user.id):
        await message.answer(f'You have chosen {users_colors[message.from_user.id]} colors')
    else:
        await message.answer(f'You have not chosen any colors')

@dp.message_handler(commands=['clear'])
async def clear_colors(message: types.Message): 
    if users_colors.get(message.from_user.id):
        users_colors[message.from_user.id] = []
        await message.answer(f'You have cleared all colors')
    else:
        await message.answer(f'You have not chosen any colors')

@dp.message_handler(commands=['all'])
async def send_all_colors(message: types.Message):
    await message.answer(f'All colors: {color_list}')

@dp.message_handler(commands=['users'])
async def send_users(message: types.Message):
    await message.answer(f'Users: {users_colors}')
    

@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    print(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
    if message.text.lower() in color_list:
        if users_colors.get(message.from_user.id):
            users_colors[message.from_user.id].append(message.text)
        else:
            users_colors[message.from_user.id] = [message.text]
        await message.answer(f'You have chosen {message.text} color')
    elif message.text.lower() == 'admin':
        await message.answer(f'You are admin\nYour id: {message.from_user.id}')
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)