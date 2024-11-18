import re
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Функция для получения последних 20 постов из сообщества
def get_vk_posts(group_id, access_token):
    url = f"https://api.vk.com/method/wall.get?owner_id=-{group_id}&count=20&access_token={access_token}&v=5.131"
    response = requests.get(url)
    data = response.json()
    
    # Выводим полученные данные для отладки
    print("Полученные данные:", data)
    
    if 'response' in data:
        return data['response']['items']
    else:
        print("Ошибка при получении постов:", data)
    return []

# Функция для проверки постов на наличие времени и даты
def extract_markers_and_links(posts):
    results = []
    time_pattern = r"\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b"  # Время в формате ЧЧ:ММ
    date_pattern = r"\b(\d{1,2}\s[а-яА-Я]+|\d{2}\.\d{2}(\.\d{4})?)\b"  # Дата в формате "2 ноября" или "02.11"
    
    for post in posts:
        text = post.get('text', '')
        print(f"Пост: {text}")  # Для отладки: выводим текст поста
        
        if text:
            # Поиск маркеров времени и даты
            times = re.findall(time_pattern, text)
            dates = re.findall(date_pattern, text)

            # Если в тексте есть маркеры времени или даты
            if times or dates:
                # Собираем маркеры в строку
                markers = ", ".join(times + [d[0] for d in dates])
                # Формируем ссылку на пост
                post_id = post['id']
                owner_id = post['owner_id']
                link = f"https://vk.com/wall{owner_id}_{post_id}"
                # Сохраняем результат
                results.append(f"{markers}: {text[:100]}... {link}")
    return results

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    group_id = '142200314'  # ID группы "tyumen.university"
    access_token = 'bb6172efbb6172efbb6172efe0b843d997bbb61bb6172efdc443297c85f52ea38831bd1'  # Ваш сервисный токен
    posts = get_vk_posts(group_id, access_token)
    # Обрабатываем посты, чтобы найти нужные маркеры и ссылки
    results = extract_markers_and_links(posts)
    
    if results:
        message = "\n\n".join(results)
    else:
        message = "Не найдено постов с указанными маркерами."
    
    await update.message.reply_text(message)

# Основной код для запуска бота
def main():
    # Создаем приложение с вашим токеном
    application = ApplicationBuilder().token("7822316799:AAHkrOT1ma0fA8wNnUf0Jo1DVsL3TiVtBEE").build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    print("start on https://t.me/tgbotutmn_bot")
    main()
