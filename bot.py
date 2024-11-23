import os
import emoji
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from modeus import Modeus

UTMN_TL_TOKEN = os.environ["UTMN_TL_TOKEN"]
UTMN_TL_BOT_NAME = os.environ["UTMN_TL_BOT_NAME"]

# Обработчик команды /start
async def start(update: Update, context):
    # message = "Привет!"
    # await update.message.reply_text(message)

    # from vk import VK
    # vk = VK()
    # await update.message.reply_text(vk.make_message())

    # Создаем кнопки
    keyboard = [
        [
            InlineKeyboardButton("Расписание на сегодня", callback_data='today'),
            InlineKeyboardButton("Расписание на неделю", callback_data='week')
        ]
    ]
    # Создаем разметку для кнопок
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Отправляем сообщение с кнопками
    await update.message.reply_text(emoji.emojize("Выберите кнопку :blush:", language="alias"), reply_markup=reply_markup)

# Обработчик нажатий на кнопки
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    modeus = Modeus()    
    # Определяем, какая кнопка была нажата
    if query.data == 'week':
        modeus.search()
        events = modeus.get_events()
        text = "\n".join(events) + emoji.emojize("\n :thumbs_up:", language="alias")
        await query.edit_message_text(text)
    elif query.data == 'today':
        text = emoji.emojize("""Вы нажали кнопку "Расписание на сегодня" :thumbs_up:""", language="alias")
        await query.edit_message_text(text)

# Основной код для запуска бота
def main():
    # Создаем приложение с вашим токеном
    application = ApplicationBuilder().token(UTMN_TL_TOKEN).build()
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    print(f"start on https://t.me/{UTMN_TL_BOT_NAME}")
    main()
