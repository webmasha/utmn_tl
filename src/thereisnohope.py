import telebot
import os
import pandas as pd
import requests
import bs4

working_dirrectory = os.path.realpath(__file__).removesuffix('bot.py')
dirrectory_files= os.listdir(working_dirrectory)
FILENAME = working_dirrectory+'user_data.csv'

#в файле user_data.csv хранятся данные о пользователях, память бота
if 'user_data.csv' in dirrectory_files:
    print('user data is found')
else:
    print('user data is missing, creating new file...')
    df = pd.DataFrame(columns=['id', 'name'])
    df.to_csv(FILENAME, index=False)

#Добавить или обновить данные об имени пользователя
def add_user(user_id, name):
    df = pd.read_csv(FILENAME)
    user_exists_check = user_exists(user_id)
    try:
        if user_exists_check != None:
            df.loc[df['id'] == user_id, 'name'] = name
            print(f"Данные о пользователе {user_id} были обновленны")
        else:
            new_user = pd.DataFrame([[user_id, name]], columns=['id', 'name'])
            df = pd.concat([df, new_user], ignore_index=True)
            df.to_csv(FILENAME, index=False)
            print(f"Пользователь {name} с ID {user_id} добавлен.")
    except ValueError:
        new_user = pd.DataFrame([[user_id, name]], columns=['id', 'name'])
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(FILENAME, index=False)
        print(f"Пользователь {name} с ID {user_id} добавлен.")
#Проверяет наличие пользователя по его id и возвращает его имя, если нет - None
def user_exists(user_id):
    df = pd.read_csv(FILENAME)
    if user_id in df['id'].values:
        return df.loc[df['id']== user_id, 'name']
    else:
        return None

def getRandomJoke():
    page = requests.get('https://www.anekdot.ru/random/anekdot/')
    if page.status_code == 200:
        print('connection is succesfull')
    else:
        print('connection have failed')
        return 'connection have failed'
    soup = bs4.BeautifulSoup(page.text,'html.parser')
    Joke = str(soup.find('div', class_='text'))
    Joke = Joke.replace('<div class="text">','')
    Joke = Joke.replace('<br/>','\n')
    Joke = Joke.replace('</div>','')
    return Joke


bot = telebot.TeleBot('7541457982:AAGvdzslraoSgSKhtscXlLQDl_4wR-O1tgw', parse_mode=None)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id,'say your name')
    bot.register_next_step_handler(message,name)
def name(message):
    bot.send_message(message.from_user.id,f'hi {message.text},i will remmember it')
    add_user(message.from_user.username,message.text)

@bot.message_handler(commands=['saymyname'])
def start_command_name(message):
    try:
        user_exists(message.from_user.username)
        bot.send_message(message.from_user.id,f'{user_exists(message.from_user.username)[0]}')
    except:
        bot.send_message(message.from_user.id,'idk, dude')
bot.infinity_polling()
