telebot, requests

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("")

update_log = "в этом обновлении была добавленна команда /update! за обновлениями можете следить в моём аккаунте GitHub 88phantom88"
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!ты можешь узнать какие комманды тут есть благодаря /commands!')

@bot.message_handler(commands=['name'])
def send_name(message):
    bot.reply_to(message, 'Привет! Меня зовут knoba!')


# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/kak_pervie_programmisti_programmirovali.jpeg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem2'])
def send_mem(message):
    with open('images/9e58e8a14f56f11ad66fa46b6d81407e.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['commands'])
def send_name(message):
    bot.reply_to(message, 'hello, name, heh(число), mem, mem2, duck, update')

@bot.message_handler(commands=["update"])
def update(message):
    bot.reply_to(message,update_log)



# Запуск бота
bot.polling()
