import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

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
            InlineKeyboardButton("Кнопка 1", callback_data='button1'),
            InlineKeyboardButton("Кнопка 2", callback_data='button2')
        ]
    ]
    # Создаем разметку для кнопок
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Отправляем сообщение с кнопками
    await update.message.reply_text("Выберите кнопку:", reply_markup=reply_markup)

# Обработчик нажатий на кнопки
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    # Определяем, какая кнопка была нажата
    if query.data == 'button1':
        await query.edit_message_text(text="Вы нажали кнопку 1!")
    elif query.data == 'button2':
        await query.edit_message_text(text="Вы нажали кнопку 2!")

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
