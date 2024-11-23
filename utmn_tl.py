import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from vk import VK

UTMN_TL_TOKEN = os.environ["UTMN_TL_TOKEN"]
UTMN_TL_BOT_NAME = os.environ["UTMN_TL_BOT_NAME"]

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "Привет!"
    await update.message.reply_text(message)
    # vk = VK()
    # await update.message.reply_text(vk.make_message())

# Основной код для запуска бота
def main():
    # Создаем приложение с вашим токеном
    application = ApplicationBuilder().token(UTMN_TL_TOKEN).build()
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    print(f"start on https://t.me/{UTMN_TL_BOT_NAME}")
    main()
