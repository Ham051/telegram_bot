
import string

from aiogram import types, Dispatcher
from create_bot import dp


#@dp.message_handler()
#async def echo_send(message: types.Message):
#    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split('')} \
 #           .intersection(set(json.load(open('cenz.json')))) != set():
  #      await message.reply('Маты_запрещены')
   #     await message.delete()

# Список матов которые нужно удалять
blacklist=['бля','хуй','пизд','пидар','сука','суки','чёрт']

# Перехват чужих сообщений в чате
#@bot.message_handler(content_types=["text"])
async def echo_send(message):
    # По очереди ищем маты из списка в сообщении
    for x in blacklist:
        if(x in message.text):
            # Если найдены маты удаляем сообщение с ними
            await message.reply('Маты запрещены')
            await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
