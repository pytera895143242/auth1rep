from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 1045832338
id_chat= '-1001419126428'

@app.on_message(filters.text)
async def payments (client,message):
    if message.from_user.id == my_id and message.text == 'Аа':
        await app.edit_message_text(message_id=message.message_id,chat_id=message.chat.id,text="""Реквизиты для оплаты спринта, просто нажми и они сохраняться👌💃🏼

🇷🇺Сбербанк - <pre>4817760152002113</pre>

🇷🇺Тинькофф - <pre>5536914049813144</pre>

🇰🇬Mbank online - <pre>996772187870</pre>

🇰🇬Элсом - <pre>0770350099</pre>

🇺🇿Uzcard - <pre>8600120420267414</pre>

🇺🇦Monobank - <pre>4441114441436100</pre>

🇰🇿Каспи - <pre>77051004909</pre>

▫️Киви - <pre>79183561047</pre>
▫️Юмани  - <pre>410019301888334</pre>

Стоимость - 9$
🇷🇺 652₽
🇰🇬 763 сом
🇺🇿 96 200 сум 
🇺🇦 237 гривен
🇰🇿 3820 тенге
Курс если изменился, не проблема😉 меняй)) 

Если с другой страны, напиши с какой  решим)
Как оплатишь, чек, или скрин оплаты отправь мне 😎 
После добавлю тебя в спринт⚡️""",parse_mode='html')

    if message.from_user.id == my_id and message.text == 'Пп':
        await app.delete_messages(chat_id=message.chat.id,message_ids=message.message_id)
        id_user = message.chat.id
        # try:
        await app.add_chat_members(chat_id=id_chat,user_ids=id_user)
        await app.send_message(chat_id=message.chat.id, text='Ееееее 🥳🥳🥳 всё добавил тебя, глянь чат)) там вся информация)))')
        # except:
        #     await app.send_message(chat_id=message.chat.id, text="""Не могу добавить, так как тебя запрещено приглашать в беседы.
#
# Что бы это исправить переходи в настройки телеграма:
#
# - Конфидециальность
# - Группы и каналы
# И добавь меня в список тех, кто тебя может приглашать в группы и каналы)
# Либо, открой доступ для всех, так
# быстрей 😅
#
# После этого напиши мне, и мы повторим попытку😎""")

app.run()